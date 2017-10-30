from rest_framework import serializers
from .models import User, ExerciseName, Exercise, Workout

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        #fields = ('id', 'first_name', 'last_name', 'email', 'date_joined')
        fields = '__all__'

class ExerciseNameSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ExerciseName
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Exercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Workout
        fields = '__all__'
