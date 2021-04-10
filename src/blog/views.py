import django_filters
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication

from .models import Blog
from . import serializers


class TitleFilter(django_filters.FilterSet):
    def __init__(self, *args, name=None, **kwargs):
        super().__init__(*args, **kwargs)

    name = django_filters.Filter(field_name='title', lookup_expr='icontains')

    class Meta:
        fields = ['title']


class BlogViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.BlogSerializer
    permission_classes = (AllowAny, )
    queryset = Blog.objects.all()

    @action(detail=False)
    def title(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = serializers.BlogTitleSerializer(queryset, many=True)
        return Response(serializer.data)