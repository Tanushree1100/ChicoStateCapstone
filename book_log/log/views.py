from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from log.forms import JoinForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Book, ReadingList
import requests
from django.http import HttpResponseBadRequest
def landing_page(request):
    return render(request, 'log/landing_page.html')

def join(request):
    if request.method == "POST":
        join_form = JoinForm(request.POST)
        if join_form.is_valid():
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = {"join_form": join_form}
            return render(request, 'log/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'log/join.html', page_data)

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                # Check if the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If the account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                return render(request, 'log/login.html', {"login_form": LoginForm})
    else:
        # Nothing has been provided for username or password.
        return render(request, 'log/login.html', {"login_form": LoginForm})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect('/')

class BookSearchView(View):
    template_name = 'log/book_search.html'

    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            books = self.search_books(query)
        else:
            books = []
        return render(request, self.template_name, {'books': books, 'query': query})

    def search_books(self, query):
        # Use Google Books API to search for books
        api_key = 'AIzaSyDlY3qJ1D4B4Ltd-QwLaNUwz0KpQKvm9QY'
        base_url = 'https://www.googleapis.com/books/v1/volumes'
        params = {'q': query, 'key': api_key}
        response = requests.get(base_url, params=params)
        data = response.json()

        # Process the API response and extract relevant information
        books = []
        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            book = Book(
                title=volume_info.get('title', ''),
                author=', '.join(volume_info.get('authors', [])),
                published_date=volume_info.get('publishedDate', ''),
                description=volume_info.get('description', ''),
                isbn=volume_info.get('industryIdentifiers', [{}])[0].get('identifier', ''),
                page_count=volume_info.get('pageCount', 0),
                thumbnail_url=volume_info.get('imageLinks', {}).get('thumbnail', ''),
                info_link=volume_info.get('infoLink', ''),
            )
            books.append(book)
        return books