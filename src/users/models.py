from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from core import helpers

class Profile(TimeStampedModel):
    uid = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE
    )
    roles = models.ManyToManyField(
        'Roles', verbose_name='角色', blank=True, related_name='profile_set'
    )
    introduction = models.CharField(
        max_length=200, blank=True, verbose_name='介紹'
    )
    avatar = models.FileField("頭像", null=True, blank=True, upload_to=helpers.upload_handle)
    name = models.CharField(max_length=200, blank=True, verbose_name='名稱')

    class Meta:
        verbose_name = 'API資料'
        verbose_name_plural = 'API資料'
        ordering = ['uid__username']

    def __str__(self):
        return self.uid.username


class Roles(TimeStampedModel):
    code = models.CharField('角色代碼', max_length=20, unique=True)
    title = models.CharField('角色名稱', max_length=255, unique=True)

    class Meta:
        verbose_name = '角色管理'
        verbose_name_plural = '角色管理'

    def __str__(self):
        return "%s" % (self.title)