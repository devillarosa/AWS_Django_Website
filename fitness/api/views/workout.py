from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from fitness.models import Workout
from fitness.api.serializers import WorkoutSerializer

# api/userexerciselist/

class WorkoutView(APIView):

    def get(self, request):
        workout = Workout.objects.all()
        serializer = WorkoutSerializer(workout, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data['user']
        exercise = request.data['exercise']
        date = request.data['date']
        weight = request.data['weight']
        serializer = WorkoutSerializer(data=request.data)

        if Workout.objects.filter(user=user, exercise=exercise, date=date, weight=weight).count():
            return HttpResponse("Entry already exists", status=400)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetailsView(APIView):

    def get(self, request, pk):
        exercise = get_object_or_404(Exercise, pk=pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def put(self, request, pk):
        exercise = get_object_or_404(Exercise, pk=pk)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        exercise = get_object_or_404(Exercise, pk=pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
