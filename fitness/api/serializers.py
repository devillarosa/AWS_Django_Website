from rest_framework import serializers
from fitness.models import Exercise, UserExercise, Workout

class UserExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserExercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Workout
        fields = '__all__'

    def get_user(self, obj):
        return str(obj.user.username)
