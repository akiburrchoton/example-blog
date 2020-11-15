from .views import *
from django.urls import path

urlpatterns = [
    path('register/', register_Api, name='register_API')
]