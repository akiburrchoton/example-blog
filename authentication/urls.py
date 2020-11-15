from authentication.views import *
from django.urls import path, include

urlpatterns = [
    path('login/', loginnn, name='login'),
    path('logout/', logouttt, name='logout'),
    path('register/', register, name='register'),
    path('api/', include('api.urls')),
]
