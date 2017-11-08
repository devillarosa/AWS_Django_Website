from rest_framework import serializers
from fitness.models import ExerciseName, Exercise, Workout

class ExerciseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseName
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(read_only=True)

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
