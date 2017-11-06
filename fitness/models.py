# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models

class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.IntegerField()
    reps = models.IntegerField()
    completed_sets = models.IntegerField()
    max_sets = models.IntegerField()

    def __str__(self):
        return " {name} - {weight} lbs, {reps} reps, {completed_sets} out of {max_sets} sets".format(
        name=self.name,
        weight=self.weight,
        reps=self.reps,
        completed_sets=self.completed_sets,
        max_sets=self.max_sets,
        )


