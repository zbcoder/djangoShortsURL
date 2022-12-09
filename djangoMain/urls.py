
from django.urls import path
from .views import *

urlpatterns = [
    path(r'profile/', myprofile, name='profile'),
    path(r'create_link/', create_link, name='create_link'),
    path(r'', home, name='home'),
    path(r'about/', about, name='about')
]
