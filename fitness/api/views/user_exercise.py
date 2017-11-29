from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from fitness.models import UserExercise
from fitness.api.serializers import UserExerciseSerializer

# api/userexerciselist/

class UserExerciseView(APIView):

    def get(self, request):
        user_exercise = UserExercise.objects.all()
        serializer = UserExerciseSerializer(user_exercise, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data['user']
        exercise = request.data['exercise']

        if UserExercise.objects.filter(user=user, exercise=exercise).count():
            return HttpResponse("Entry already exists", status=400)

        serializer = UserExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserExerciseDetailsView(APIView):

    def get(self, request, pk):
        user_exercise = get_object_or_404(UserExercise, pk=pk)
        serializer = UserExerciseSerializer(user_exercise)
        return Response(serializer.data)

    def delete(self, request, pk):
        user_exercise = get_object_or_404(UserExercise, pk=pk)
        user_exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
