
from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', myprofile, name='profile'),
    path('create_link/', create_link, name='create_link'),
    path('', home, name='home'),
    path('about/', about, name='about')
]
