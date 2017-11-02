from django.contrib.auth.models import User
from rest_framework import serializers
from fitness.models import ExerciseName, Exercise, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ExerciseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseName
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Workout
        fields = '__all__'

    def get_user(self, obj):
        return str(obj.user.username)
