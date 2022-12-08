from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'register/', register, name='register'),
    path(r'', include('django.contrib.auth.urls'))
]
