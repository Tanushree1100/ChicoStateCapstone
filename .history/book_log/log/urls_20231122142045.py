from django.urls import path
from . import views as log_views

urlpatterns = [
    path('join/', log_views.join),
    path('login/', log_views.user_login),
    path('logout/', log_views.user_logout),
    # Add other URL patterns specific to the log app
]
