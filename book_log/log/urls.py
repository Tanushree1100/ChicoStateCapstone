# log/urls.py
from django.contrib import admin
from django.urls import path,include
# log/urls.py
from .views import landing_page, BookSearchView


urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('book_search/', BookSearchView.as_view(), name='book_search'),
]
    # Add other urlpatterns as needed

