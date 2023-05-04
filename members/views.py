from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and  user.is_superuser:
            login(request, user)
            return redirect('rules_admin')
        elif user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "You may had entered an invalid username or password, Try Again...")
            messages.success(request, "Account may be deactivated by the admin...")
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request):
    messages.success(request, "You Are Now Logged Out...")
    logout(request)
    return redirect('home')

