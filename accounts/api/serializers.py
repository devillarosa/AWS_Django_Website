from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=6, max_length=100,
            write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=True, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {'password' : {'write_only': True}}

    def validate(self, data):
        user_obj = None
        username = data.get('username', None)
        password = data.get('password', None)
        if not username or not password:
            raise ValidationError("A username/password is required to login")

        user = User.objects.filter(Q(username=username)).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Invalid username")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")

    #    data["token"] = "SOME RANDOM TOKEN"
        return data
