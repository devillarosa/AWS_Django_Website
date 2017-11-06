# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    return render(request, 'accounts/login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'accounts/login.html')
    else:
        pass
    return render(request, 'accounts/login.html', {'error_message' : 'Invalid login'})

def logout_user(request):
    logout(request)
    return render(request, 'accounts/login.html')

