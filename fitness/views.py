# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View

def home_page(request):
    if request.user.is_authenticated():
        return render(request, 'fitness/home.html')
    else:
        return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

def exercise_page(request):
    if request.user.is_authenticated():
        return render(request, 'fitness/exercise.html')
    else:
        return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

def workout_page(request):
    if request.user.is_authenticated():
        return render(request, 'fitness/workout.html')
    else:
        return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

def history_page(request):
    if request.user.is_authenticated():
        return render(request, 'fitness/history.html')
    else:
        return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')
