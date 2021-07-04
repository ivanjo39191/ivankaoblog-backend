from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, BlogType, BlogSubtype, BlogTag
from .forms import BlogForm

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    def get_types(self, obj):
        return "、".join([p.type_name for p in obj.types.all()])
        
    form = BlogForm
    list_display = ('title', 'get_types', 'created')
    list_filter = ['types', 'subtypes', 'tags']
    search_fields = ['title',]


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    def count(self, obj):
        return obj.blog_set.count()

    list_display = ('type_name', 'count')


@admin.register(BlogSubtype)
class BlogSubtypeAdmin(admin.ModelAdmin):
    def count(self, obj):
        return obj.blog_set.count()

    list_display = ('subtype_name', 'type', 'count')


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    def count(self, obj):
        return obj.blog_set.count()

    list_display = ('tag_name', 'count')