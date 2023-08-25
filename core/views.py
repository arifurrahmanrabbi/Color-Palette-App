from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        #If user is logged in show home page
        return render(request, 'home.html')
    #Else redirect to login page
    return redirect('login')

def login_user(request):
    #If user is trying to log in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
        else:
            #If user is not found
            messages.success(request, "Error")
        #Redirect to Home page
        return redirect('home')
    #Else show the login page
    return render(request, 'login.html')

def logout_user(request):
    #Logout user
    logout(request)
    messages.success(request, "Logged Out")
    #Redirect to login page
    return redirect('login')
