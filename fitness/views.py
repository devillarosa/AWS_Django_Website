# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializers import UserSerializer, ExerciseNameSerializer, ExerciseSerializer, WorkoutSerializer
from .models import ExerciseName, Exercise, Workout

def index(request):
    return render(request, 'fitness/index.html')


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExerciseNameCreateView(generics.ListCreateAPIView):
    queryset = ExerciseName.objects.all()
    serializer_class = ExerciseNameSerializer

    def perform_create(self, serializer):
        serializer.save()

class ExerciseNameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseName.objects.all()
    serializer_class = ExerciseNameSerializer

class ExerciseCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        serializer.save()

class ExerciseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutCreateView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save()

class WorkoutDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
