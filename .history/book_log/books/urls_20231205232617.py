# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('book_detail/<int:pk>/', book_detail, name='book_detail'),
    path('book_new/', book_new, name='book_new'),
    path('book_edit/<int:pk>/', book_edit, name='book_edit'),
    path('book_delete/<int:pk>/', book_delete, name='book_delete'),
    path('books/book_finish_reading/<int:book_id>/', views.book_finish_reading, name='book_finish_reading'),
    path('completed_books/', completed_books, name='completed_books'),  # New URL pattern
]

