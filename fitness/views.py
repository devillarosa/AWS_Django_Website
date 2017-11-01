# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View

from .forms import UserForm

def index(request):
    return render(request, 'fitness/login.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'fitness/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #Creates an object from the form. Doesn't save it to the database yet. Stores it locally
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # Save to the database
            user.save()

            # returns User objects if credientials are correct
            user = authenicate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('fitness:index')
        else:
            return render(request, self.template_name, {'form':form})

