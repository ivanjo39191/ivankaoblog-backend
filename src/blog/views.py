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

from .models import Blog, BlogSetting, HomeCarousel, BlogType
from . import serializers


class TitleFilter(django_filters.FilterSet):
    def __init__(self, *args, name=None, **kwargs):
        super().__init__(*args, **kwargs)

    name = django_filters.Filter(field_name='title', lookup_expr='icontains')

    class Meta:
        fields = ('title',)

class TitleFilter(django_filters.FilterSet):
    def __init__(self, *args, name=None, **kwargs):
        super().__init__(*args, **kwargs)
    id = django_filters.Filter(field_name='id', lookup_expr='exact')
    title = django_filters.Filter(field_name='title', lookup_expr='exact')
    class Meta:
        fields = ['id', 'title']

class TypeFilter(django_filters.FilterSet):
    def __init__(self, *args, type=None, **kwargs):
        super().__init__(*args, **kwargs)

    types = django_filters.Filter(field_name='types__type_name', lookup_expr='iexact')
    subtypes = django_filters.Filter(field_name='subtypes__subtype_name', lookup_expr='iexact')
    tags = django_filters.Filter(field_name='tags__tag_name', lookup_expr='iexact')

    class Meta:
        fields = ('types', 'subtypes', 'tags')


class BlogViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.BlogSerializer
    permission_classes = (AllowAny, )
    queryset = Blog.objects.filter(status__name='公開').order_by('-publisher_date')

    def filter_queryset(self, queryset):
        if self.action == 'blogtype':
            self.filterset_class = TypeFilter
        return super().filter_queryset(queryset)

    @action(detail=False)
    def title(self, request):
        
        queryset = self.filter_queryset(self.get_queryset())[0:20]
        serializer = serializers.BlogTitleSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def blogtype(self, request):
        queryset = self.filter_queryset(self.get_queryset())[0:20]
        serializer = serializers.BlogTitleSerializer(queryset, many=True)
        return Response(serializer.data)

class BlogSettingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BlogSettingSerializer
    permission_classes = (AllowAny, )
    queryset = BlogSetting.objects.filter(active=True).order_by('order')[0:1]

class HomeCarouselViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.HomeCarouselSerializer
    permission_classes = (AllowAny, )
    queryset = HomeCarousel.objects.filter(active=True).order_by('order')
    
class BlogTypeViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.BlogTypeSerializer
    permission_classes = (AllowAny, )
    queryset = BlogType.objects.filter(is_home=True).order_by('order')

