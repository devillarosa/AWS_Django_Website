# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    """This class represents the users login model"""
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)

class Exercise(models.Model):
    """This class represents the exercise"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Workout(models.Model):
    """This class represents the Workout for an exercise"""
    date = models.DateField()
    name = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.IntegerField()
    reps = models.IntegerField()
    completed_sets = models.IntegerField()
    max_sets = models.IntegerField()

    def __str__(self):
        return "{date}: {name} - {weight} lbs, {reps} reps, {completed_sets} out of {max_sets} sets".format(
            date=self.date,
            name=self.name,
            weight=self.weight,
            reps=self.reps,
            completed_sets=self.completed_sets,
            max_sets=self.max_sets,
            )
