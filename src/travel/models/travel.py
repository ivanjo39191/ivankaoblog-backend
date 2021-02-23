from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

__all__ = ('Travel', 'Rating')


class Travel(TimeStampedModel):
  title = models.CharField(max_length=80, blank=True)
  description = models.TextField(max_length=300, blank=True)
  url = models.URLField(blank=True)
  category = models.CharField(max_length=50, blank=True)
  subcategory = models.TextField(max_length=50, blank=True)
  author = models.TextField(max_length=50, blank=True)

  def rating_average(self):
    sum=0
    ratings = Rating.objects.filter(travel=self)
    for rating in ratings:
      sum = sum + rating.stars
    if len(ratings) > 0:
      return sum/len(ratings)
    else:
      return 0
  
  def comments_list(self):
    allcomments = Rating.objects.filter(travel=self)
    listallcomments = []
    for comment in allcomments:
      print(comment.comments)
      listallcomments.append(comment.comments)
    return listallcomments

class Rating(TimeStampedModel):
  travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
  user = models.ForeignKey (User, on_delete=models.CASCADE)
  stars = models.IntegerField()
  comments = models.TextField(max_length=300, blank=True)

  class Meta:
    unique_together = (('user','travel'),)
    index_together = (('user','travel'),)