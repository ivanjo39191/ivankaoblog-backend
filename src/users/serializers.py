from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Profile, Roles


class RolesSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.title

    class Meta:
        model = Roles


class ProfileSerializer(serializers.ModelSerializer):
    roles = RolesSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        print(user)
        Token.objects.create(user=user)
        return user