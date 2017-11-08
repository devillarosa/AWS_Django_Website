# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ExerciseName, Exercise, Workout

# Register your models here.
admin.site.register(ExerciseName)
admin.site.register(Exercise)
admin.site.register(Workout)
