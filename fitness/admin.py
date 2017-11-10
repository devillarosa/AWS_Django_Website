# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Exercise, UserExercise, Workout

# Register your models here.
admin.site.register(Exercise)
admin.site.register(UserExercise)
admin.site.register(Workout)
