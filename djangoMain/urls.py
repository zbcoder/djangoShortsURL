
from django.urls import path
from .views import *

urlpatterns = [
    path(r'myprofile/', myprofile, name='myprofile'),
    path(r'create_link/', create_link, name='create_link')
]
