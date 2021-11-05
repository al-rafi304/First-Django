from django.db import models
from django.db.models.base import Model

# Create your models here.
class Result(models.Model):
    name        = models.CharField(default='Your name', max_length=50)
    science     = models.IntegerField()
    english     = models.IntegerField()
    history     = models.IntegerField()
    has_passed  = models.BooleanField(default=True)