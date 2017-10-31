# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'fitness/index.html')
