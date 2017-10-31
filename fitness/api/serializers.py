from django.contrib.auth.models import User
from rest_framework import serializers
from fitness.models import ExerciseName, Exercise, Workout

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ExerciseNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseName
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = '__all__'
