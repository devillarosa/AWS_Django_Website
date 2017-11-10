# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models

class Exercise(models.Model):
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name

class UserExercise(models.Model):
    user = models.ForeignKey(User)
    exercise = models.ForeignKey(Exercise)

    def __str__(self):
        return self.user.username + " - " + self.exercise.name

class Workout(models.Model):
    user = models.ForeignKey(User)
    exercise = models.ForeignKey(Exercise)
    date = models.DateField()
    weight = models.IntegerField()
    reps = models.IntegerField()
    completed_sets = models.IntegerField()
    max_sets = models.IntegerField()
