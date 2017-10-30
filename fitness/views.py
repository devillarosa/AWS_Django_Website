# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import UserSerializer, ExerciseSerializer
from .models import User, Exercise

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
