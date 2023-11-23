from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse  # Import HttpResponse
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()[:5]
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Check if adding the book exceeds the limits to the list.
            if Book.objects.count() >= 5:
                message = 'Cannot add more than 5 books to the list.'
                return HttpResponse(message)

            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()

    return HttpResponse(render(request, 'books/book_edit.html', {'form': form}))

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
