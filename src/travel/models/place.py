from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

__all__ = ('Place',)


class Place(TimeStampedModel):
    json_d = models.CharField(max_length=80, null=True, blank=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    zone = models.CharField(max_length=80, null=True, blank=True)
    toldescribe = models.TextField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    add = models.CharField(max_length=80, null=True, blank=True)
    zipcode = models.CharField(max_length=80, null=True, blank=True)
    region = models.CharField(max_length=80, null=True, blank=True)
    town = models.CharField(max_length=80, null=True, blank=True)
    tel = models.CharField(max_length=80, null=True, blank=True)
    travellinginfo = models.TextField(max_length=300, null=True, blank=True)
    opentime = models.CharField(max_length=300, null=True, blank=True)
    website = models.CharField(max_length=300, null=True, blank=True)
    picture1 = models.URLField(blank=True)
    picdescribe1 = models.TextField(max_length=300, null=True, blank=True)
    picture2 = models.URLField(blank=True)
    picdescribe2 = models.TextField(max_length=300, null=True, blank=True)
    picture3 = models.URLField(blank=True)
    picdescribe3 = models.TextField(max_length=300, null=True, blank=True)
    gov = models.CharField(max_length=80, null=True, blank=True)
    px = models.CharField(max_length=80, null=True, blank=True)
    py = models.CharField(max_length=80, null=True, blank=True)
    orgpclass = models.CharField(max_length=80, null=True, blank=True)
    pclass1 = models.CharField(max_length=80, null=True, blank=True)
    pclass2 = models.CharField(max_length=80, null=True, blank=True)
    pclass3 = models.CharField(max_length=80, null=True, blank=True)
    map = models.CharField(max_length=80, null=True, blank=True)
    parkinginfo = models.CharField(max_length=300, null=True, blank=True)
    parkinginfo_px = models.CharField(max_length=80, null=True, blank=True)
    parkinginfo_py = models.CharField(max_length=80, null=True, blank=True)
    ticketinfo = models.TextField(max_length=300, null=True, blank=True)
    remarks = models.TextField(max_length=300, null=True, blank=True)
    keyword = models.TextField(max_length=300, null=True, blank=True)
    changetime = models.DateTimeField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-modified']