from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book
from .forms import BookForm, ReviewForm
from django.db.models import Q

def book_list(request):
    # Retrieve the book list from the session
    book_list = request.session.get('book_list', [])

    # Filter books based on whether they are finished reading or not
    books = Book.objects.filter(pk__in=book_list)
    
    completed_books_ids = request.session.get('completed_books', [])
    completed_books = Book.objects.filter(pk__in=completed_books_ids)
    
    return render(request, 'books/book_list.html', {'books': books, 'completed_books': completed_books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()

            # Add the new book to the book list in the session
            book_list = request.session.get('book_list', [])
            book_list.append(book.pk)
            request.session['book_list'] = book_list

            # Redirect to the book detail page for the newly created book
            return redirect('book_detail', pk=book.pk)
        else:
            print(form.errors)  # Debugging statement
    else:
        form = BookForm()

    return render(request, 'books/book_edit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

def completed_books(request):
    completed_books_ids = request.session.get('completed_books', [])
    completed_books = Book.objects.filter(pk__in=completed_books_ids)
    return render(request, 'books/completed_books.html', {'completed_books': completed_books})



def book_finish_reading(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        # Check if the book is marked as finished
        if request.POST.get('finished_reading') == 'true':
            book.finished_reading = True
            book.save()

            # Update the session to store the completed book ID
            completed_books = request.session.get('completed_books', [])
            completed_books.append(book.pk)
            request.session['completed_books'] = completed_books

            # Remove the book from the regular book list
            books = Book.objects.filter(Q(finished_reading=True) | Q(finished_reading=False)).exclude(pk=book.pk)

            # Update the book list in the session
            book_list = [book.pk for book in books]
            request.session['book_list'] = book_list

            return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def write_review(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return render(request, 'books/save_review.html')
    else:
        form = ReviewForm()

    return render(request, 'books/write_review.html', {'book': book, 'form': form})
def save_review(request):
    # Your logic for handling the save_review view goes here
    return render(request, 'books/save_review.html') 