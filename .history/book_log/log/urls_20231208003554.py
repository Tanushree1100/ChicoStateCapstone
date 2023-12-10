# log/urls.py

from django.urls import path
from .views import landing_page, index

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('', index, name='index'),

]
