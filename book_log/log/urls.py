# log/urls.py
from django.contrib import admin
from django.urls import path,include
# log/urls.py
from .views import landing_page, BookSearchView, join, user_login, user_logout



urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('book_search/', BookSearchView.as_view(), name='book_search'),
    path('join/', join, name='join'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    # Add other URL patterns as needed
]
    # Add other urlpatterns as needed

