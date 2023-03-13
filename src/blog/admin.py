from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Blog, BlogType, BlogSubtype, BlogTag, BlogStatus, BlogHistory, BlogSetting, HomeCarousel
from .forms import BlogForm
from .resources import BlogResource, BlogTypeResource, BlogSubtypeResource, BlogTagResource, BlogStatusResource

@admin.register(BlogHistory)
class BlogHistoryAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status__name="歷史紀錄")

    def get_types(self, obj):
        return "、".join([p.type_name for p in obj.types.all()])
        
    form = BlogForm
    list_display = ('title', 'get_types', 'modified', 'publisher_date', 'created')
    list_filter = ['types', 'subtypes', 'tags']
    search_fields = ['title',]
    fieldsets = [
        (
            None, {
                'classes': (

                ),
                'fields':
                    (
                        'title', 'subtitle', 'content', 'types', 'subtypes', 'tags', 'author', 'banner', 'publisher_date', 'status'
                    )
            }
        ),
    ]

    class Media:
        css = {
             'all': ('/static/custom/css/filteredselectmultiple.css',)
        }

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(status__name="歷史紀錄")

    def get_types(self, obj):
        return "、".join([p.type_name for p in obj.types.all()])
        
    form = BlogForm
    resource_class = BlogResource
    list_display = ('title', 'get_types', 'modified', 'publisher_date', 'created')
    list_filter = ['types', 'subtypes', 'tags']
    search_fields = ['title',]
    fieldsets = [
        (
            None, {
                'classes': (

                ),
                'fields':
                    (
                        'title', 'subtitle', 'content', 'types', 'subtypes', 'tags', 'author', 'banner', 'publisher_date', 'status'
                    )
            }
        ),
    ]

    class Media:
        css = {
             'all': ('/static/custom/css/filteredselectmultiple.css',)
        }

    def save_model(self, request, obj, form, change):
        obj.save()
        blog_history = BlogHistory.objects.create()
        blog_history.title = obj.title
        blog_history.subtitle = obj.subtitle
        blog_history.content = obj.content
        [blog_history.types.add(i) for i in obj.types.all()]
        [blog_history.subtypes.add(i) for i in obj.subtypes.all()]
        [blog_history.tags.add(i) for i in obj.tags.all()]
        blog_history.author = obj.author
        blog_history.banner = obj.banner
        blog_history.publisher_date = obj.publisher_date
        blog_history.status = BlogStatus.objects.get(name='歷史紀錄')
        blog_history.save()

        
@admin.register(BlogType)
class BlogTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def count(self, obj):
        return obj.blog_set.count()

    resource_class = BlogTypeResource
    list_display = ('type_name', 'count', 'is_home', 'order')


@admin.register(BlogSubtype)
class BlogSubtypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def count(self, obj):
        return obj.blog_set.count()

    resource_class = BlogSubtypeResource
    list_display = ('subtype_name', 'type', 'count')


@admin.register(BlogTag)
class BlogTagAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def count(self, obj):
        return obj.blog_set.count()

    resource_class = BlogTagResource
    list_display = ('tag_name', 'count')

@admin.register(BlogStatus)
class BlogStatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def count(self, obj):
        return obj.blog_set.count()

    resource_class = BlogStatusResource
    list_display = ('name', 'count')



@admin.register(BlogSetting)
class BlogSettingAdmin(admin.ModelAdmin):

    list_display = ('title', 'modified', 'created', 'active')
    search_fields = ['title',]
    fieldsets = [
        (
            None, {
                'classes': (

                ),
                'fields':
                    (
                        'title', 'subtitle', 'blogname', 'author', 'active', 'order'
                    )
            }
        ),
    ]

    class Media:
        css = {
             'all': ('/static/custom/css/filteredselectmultiple.css',)
        }


@admin.register(HomeCarousel)
class HomeCarouselAdmin(admin.ModelAdmin):

    list_display = ('title', 'modified', 'created', 'active')
    search_fields = ['title',]
    fieldsets = [
        (
            None, {
                'classes': (

                ),
                'fields':
                    (
                        'title', 'subtitle', 'author', 'banner', 'active', 'order'
                    )
            }
        ),
    ]

    class Media:
        css = {
             'all': ('/static/custom/css/filteredselectmultiple.css',)
        }