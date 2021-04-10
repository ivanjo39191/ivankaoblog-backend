from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField  #導入富文本套件

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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']