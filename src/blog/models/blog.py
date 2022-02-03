from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField  #導入富文本套件

from core import helpers

__all__ = ('Blog', 'BlogType', 'BlogSubtype', 'BlogTag', 'BlogStatus', 'BlogHistory', 'BlogSetting', 'HomeCarousel')


# Create your models here.
class BlogType(TimeStampedModel):
    type_name = models.CharField(max_length=200, null=True)
    is_home = models.BooleanField('次選單顯示', default=True)
    order = models.PositiveIntegerField(_('Order'), null=True, blank=True, default=None)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['order','type_name']


class BlogSubtype(TimeStampedModel):
    type = models.ForeignKey(BlogType, on_delete=models.CASCADE, null=True, related_name='subtype_set')
    subtype_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.type} / {self.subtype_name}'

    class Meta:
        ordering = ['type']


class BlogTag(TimeStampedModel):
    tag_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ['tag_name']

class BlogStatus(TimeStampedModel):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Blog(TimeStampedModel):

    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField()  #改為RichTextField
    types = models.ManyToManyField(BlogType, blank=True, related_name='blog_set')
    subtypes = models.ManyToManyField(BlogSubtype, blank=True, related_name='blog_set')
    tags = models.ManyToManyField(BlogTag, blank=True, related_name='blog_set')
    status = models.ForeignKey(BlogStatus,on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    banner = models.FileField("主圖片", null=True, blank=True, upload_to=helpers.upload_handle)
    publisher_date = models.DateField('發佈日期', null=True, blank=True)  # 發佈日期

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified', '-publisher_date' ]

class BlogHistory(Blog):

    def __str__(self):
        return self.title

    class Meta:
        proxy = True
        ordering = ['-modified', '-publisher_date' ]


class BlogSetting(TimeStampedModel):
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    blogname = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    logo = models.FileField("Logo", null=True, blank=True, upload_to=helpers.upload_handle)
    active = models.BooleanField(_('Active'), default=True)
    order = models.PositiveIntegerField(_('Order'), null=True, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', ]

class HomeCarousel(TimeStampedModel):
    
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    banner = models.FileField("主圖片", null=True, blank=True, upload_to=helpers.upload_handle)
    active = models.BooleanField(_('Active'), default=True)
    order = models.PositiveIntegerField(_('Order'), null=True, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', ]