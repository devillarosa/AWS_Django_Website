# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def loginPage(request):
    if request.user.is_authenticated():
            return render(request, 'fitness/home.html')
    else:
        return render(request, 'accounts/login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'fitness/home.html')
        return render(request, 'accounts/login.html', {'error_message' : 'Invalid login'})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'fitness/home.html')
    return render(request, 'accounts/login.html', {'error_message' : 'Invalid Registration'})

