from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.shortcuts import render, redirect
# LOGIN VIEW ENDPOINT

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')


@api_view(['POST',])
def register_Api(request):
    if request.method == 'POST':
        serializer = Register_Serializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save(request.data)
            data['response'] = "Successfully registered a new user"
            data['first_name'] = user.first_name
            data['email'] = user.email
        else:
            data = serializer.errors
        return Response(data)

@api_view(['GET',])
def login_Api(request):
    serializer = Login_Serializer(data=request.data)
    data = {}

    if serializer.is_valid():
        data['response'] = "User logged in  successfully"
    else:  
        data = serializer.errors

    
    # data['token'] = serializer.tokens
    # print(data)
    
    return Response(data, status=status.HTTP_200_OK)

