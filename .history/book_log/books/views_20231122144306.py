from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.filter(finished_reading=False)[:5]
    completed_books = Book.objects.filter(finished_reading=True)
    return render(request, 'books/book_list.html', {'books': books, 'completed_books': completed_books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Check if there are any books in the list
            if Book.objects.exists() and Book.objects.count() >= 5:
                message = 'Cannot add more than 5 books to the list.'
                back_button_html = '<a href="{}">Back to Book List</a>'.format(reverse('book_list'))
                return HttpResponse('{}<br>{}'.format(message, back_button_html), status=400)

            book = form.save()
            return redirect('book_detail', pk=book.pk)
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

def book_finish_reading(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.finished_reading = True
    book.save()
    return JsonResponse({'success': True})
