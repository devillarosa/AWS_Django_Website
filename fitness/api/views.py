# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import ExerciseSerializer, UserUserUserExerciseSerializer, WorkoutSerializer
from fitness.models import Exercise, UserUserUserExercise, Workout

