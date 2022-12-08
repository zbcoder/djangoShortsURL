
from django.urls import path
from .views import *

urlpatterns = [
    path(r'myprofile/', myprofile, name='myprofile')
]
