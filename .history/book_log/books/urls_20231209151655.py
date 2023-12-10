# urls.py
from django.urls import path
from .views import (
    book_list,
    book_detail,
    book_new,
    book_edit,
    book_delete,
    book_finish_reading,
    completed_books,
    write_review,
    save_review, 
    view_saved_review, # Import the save_review view
) 

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('book_detail/<int:pk>/', book_detail, name='book_detail'),
    path('book_new/', book_new, name='book_new'),
    path('book_edit/<int:pk>/', book_edit, name='book_edit'),
    path('book_delete/<int:pk>/', book_delete, name='book_delete'),
    path('books/book_finish_reading/<int:pk>/', book_finish_reading, name='book_finish_reading'),
    path('completed_books/', completed_books, name='completed_books'),
    path('write_review/<int:pk>/', write_review, name='write_review'),
    path('save_review/<int:pk>/', save_review, name='save_review'),
    path('view_saved_review/<int:pk>/', view_saved_review, name='view_saved_review'),
    # Add other URL patterns as needed
]
