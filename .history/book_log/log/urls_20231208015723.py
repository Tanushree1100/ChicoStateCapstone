# log/urls.py
from django.urls import path
from .views import landing_page, index, search_results

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('index/', index, name='index'),
    path('search-results/', search_results, name='search_results'),
]
