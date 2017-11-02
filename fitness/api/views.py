# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import ExerciseNameSerializer, ExerciseSerializer, WorkoutSerializer
from fitness.models import ExerciseName, Exercise, Workout

# Todo: Seperate Creating User from Listing User functionality
# Only admins can View users, Anyone can create users

class ExerciseNameCreateView(generics.ListCreateAPIView):
    queryset = ExerciseName.objects.all()
    serializer_class = ExerciseNameSerializer
    permissions_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class ExerciseNameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseName.objects.all()
    serializer_class = ExerciseNameSerializer

class ExerciseCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permissions_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExerciseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kargs):
        queryset = Workout.objects.filter(user=self.request.user)
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkoutDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
