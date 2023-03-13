from import_export import resources, fields, widgets
from django.contrib.auth.models import User
from .models import Blog, BlogType, BlogSubtype, BlogTag, BlogStatus, HomeCarousel, BlogSetting

from .models import Blog, BlogType, BlogSubtype, BlogTag, BlogStatus, BlogSetting, HomeCarousel


class BlogResource(resources.ModelResource):
    types = fields.Field(column_name='types', attribute='types', widget=widgets.ManyToManyWidget(BlogType, field='type_name'))
    subtypes = fields.Field(column_name='subtypes', attribute='subtypes', widget=widgets.ManyToManyWidget(BlogSubtype, field='subtype_name'))
    tags = fields.Field(column_name='tags', attribute='tags', widget=widgets.ManyToManyWidget(BlogTag, field='tag_name'))
    status = fields.Field(column_name='status', attribute='status', widget=widgets.ForeignKeyWidget(BlogStatus, 'name'))
    author = fields.Field(column_name='author', attribute='author', widget=widgets.ForeignKeyWidget(User, 'username'))

    class Meta:
        model = Blog
        fields = ('id', 'title', 'subtitle', 'content', 'types', 'subtypes', 'tags', 'status', 'author', 'banner', 'publisher_date')
        export_order = ('id', 'title', 'subtitle', 'content', 'types', 'subtypes', 'tags', 'status', 'author', 'banner', 'publisher_date')



class BlogTypeResource(resources.ModelResource):
    class Meta:
        model = BlogType
        fields = ('id', 'type_name', 'is_home', 'order',)
        export_order = ('id', 'type_name', 'is_home', 'order',)


class BlogSubtypeResource(resources.ModelResource):
    class Meta:
        model = BlogSubtype
        fields = ('id', 'type', 'subtype_name',)
        export_order = ('id', 'type', 'subtype_name',)


class BlogTagResource(resources.ModelResource):
    class Meta:
        model = BlogTag
        fields = ('id', 'tag_name',)
        export_order = ('id', 'tag_name',)


class BlogStatusResource(resources.ModelResource):
    class Meta:
        model = BlogStatus
        fields = ('id', 'name',)
        export_order = ('id', 'name',)