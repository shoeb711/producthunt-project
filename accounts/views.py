from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['passowrd1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username Already Exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(request, user)
                auth.login(request)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password Does Not Match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            user = auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and Password is Invalid'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        user = auth.logout(request)
        return redirect('home')
