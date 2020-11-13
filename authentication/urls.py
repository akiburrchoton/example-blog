from django.urls import path
from authentication.views import loginnn, register, logouttt

urlpatterns = [
    path('login/', loginnn, name='login'),
    path('logout/', logouttt, name='logout'),
    path('register/', register, name='register'),
]
