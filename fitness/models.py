# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    """This class represents the users login model"""
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
