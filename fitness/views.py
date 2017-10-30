# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import UserSerializer, ExerciseNameSerializer, ExerciseSerializer, WorkoutSerializer
from .models import User, ExerciseName, Exercise, Workout

class UserCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExerciseNameCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ExerciseName.objects.all()
    serializer_class = ExerciseNameSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ExerciseNameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = ExerciseName.objects.all()
    serializer_class = ExerciseNameSerializer

class ExerciseCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ExerciseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class WorkoutDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
