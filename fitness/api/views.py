# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import ExerciseSerializer, WorkoutSerializer
from fitness.models import Exercise, Workout

class ExerciseCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permissions_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ExerciseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permissions_classes = [IsAuthenticated]

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
        serializer.save()

class WorkoutDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permissions_classes = [IsAuthenticated]
