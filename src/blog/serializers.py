from rest_framework import serializers
from .models import Blog
from rest_framework.authtoken.models import Token


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'types', 'subtypes', 'tags', 'author', 'created', 'banner')


class BlogTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'types', 'subtypes', 'tags', 'author', 'created', 'banner')
