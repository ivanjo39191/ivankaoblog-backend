from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import Profile


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset

    serializer_class = serializers.UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Profile.objects.filter(uid=self.request.user)
        return queryset

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer