from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls'))
]
