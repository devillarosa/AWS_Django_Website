# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import UserSerializer, UserLoginSerializer

# Todo: Seperate Creating User from Listing User functionality
# Only admins can View users, Anyone can create users

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class UserLoginView(APIView):
    permissions_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
