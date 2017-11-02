from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import serializers
from fitness.models import ExerciseName, Exercise, Workout

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email2 = serializers.EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must Match")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email,
                password = password
                )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
    user_obj = None
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def validate(self, data):
        username = data.get("username", None)
        password = data['password']
        if not username:
            raise ValidationError("A username is required to login")

        user = User.objects.filter(Q(username=username)).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Invalid username")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")

        data["token"] = "SOME RANDOM TOKEN"
        return data
