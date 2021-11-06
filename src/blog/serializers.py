from rest_framework import serializers
from .models import Blog, BlogType, BlogSubtype, BlogTag, BlogSetting, HomeCarousel
from rest_framework.authtoken.models import Token


class BlogSerializer(serializers.ModelSerializer):
    types = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='type_name'
     )
    subtypes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='subtype_name'
     )
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='tag_name'
     )
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = Blog
        fields = ('id', 'title', 'subtitle', 'content', 'types', 'subtypes', 'tags', 'author', 'created', 'banner', 'publisher_date', 'status')


class BlogTitleSerializer(serializers.ModelSerializer):
    types = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='type_name'
     )
    subtypes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='subtype_name'
     )
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='tag_name'
     )
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = Blog
        fields = ('id', 'title', 'subtitle', 'types', 'subtypes', 'tags', 'author', 'created', 'banner')



class BlogSettingSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = BlogSetting
        fields = ('id', 'title', 'subtitle', 'author', 'created', 'banner',)


class HomeCarouselSerializer(serializers.ModelSerializer):
    
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = HomeCarousel
        fields = ('id', 'title', 'subtitle', 'author', 'created', 'banner',)

class BlogTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogType
        fields = ('id', 'type_name',)
