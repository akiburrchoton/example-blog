from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages

# LOGIN VIEW ENDPOINT

def loginnn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
         
        user = authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Wrong Email or Password')
            return redirect('login')

    else:
        return render(request, 'login.html')
    


def register(request):
    
    # Checks if the request method is POST 
    if request.method == 'POST':

        # Get the values from the form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm-password']

        username = email

        # Checks if passwords match
        if password1 == password2:
            # Check the username 
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User already exists!')
                return redirect('register')
            else:
                # Good to go 
                user = User.objects.create_user(username = username, first_name=first_name, last_name=last_name,password=password1, email=email)

                user.save()
                messages.success(request, 'A new user has been created successfully!')
                return redirect('login')       
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
        
        
    return render(request, 'register.html')

def logouttt(request):
    logout(request)
    return redirect('login')