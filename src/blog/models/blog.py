from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField  #導入富文本套件

from core import helpers

__all__ = ('Blog', 'BlogType')


# Create your models here.
class BlogType(TimeStampedModel):
    type_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.type_name


class Blog(TimeStampedModel):

    title = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField()  #改為RichTextField
    type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time = models.CharField(max_length=200, null=True)
    banner = models.FileField("主圖片", null=True, blank=True, upload_to=helpers.upload_handle)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']