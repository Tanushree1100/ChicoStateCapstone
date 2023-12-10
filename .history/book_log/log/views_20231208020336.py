from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from log.forms import JoinForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
import requests
from .models import Book
def landing_page(request):
    return render(request, 'log/landing_page.html')

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
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
            page_data = { "join_form": join_form }
            return render(request, 'log/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'log/join.html', page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'log/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'log/login.html', {"login_form": LoginForm})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect('/')

def search_books(query):
    base_url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'q': query, 'key': 'AIzaSyDlY3qJ1D4B4Ltd-QwLaNUwz0KpQKvm9QY'}  # Replace with your API key

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])
    else:
        print(f"Error: {response.status_code}")
        return []

# views.py

# views.py

def index(request):
    if request.method == 'POST':
        query = request.POST.get('search_query', '')
        results = search_books(query)

        # Save the search results in the database
        for book_data in results:
            title = book_data['volumeInfo']['title']
            authors = book_data['volumeInfo'].get('authors', ['Unknown Author'])
            # Ensure authors is saved as a list
            Book.objects.create(title=title, authors=authors)

        # Redirect to the search results page
        return redirect(reverse('search_results') + f'?query={query}')

    # Display the saved results on the landing page
    return render(request, 'log/landing_page.html', {'search_results': [], 'saved_results': Book.objects.all(), 'query': ''})




def search_results(request):
    query = request.GET.get('query', '')
    results = search_books(query)
    return render(request, 'log/search_results.html', {'results': results, 'query': query})