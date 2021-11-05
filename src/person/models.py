from django.db import models
from django.db.models.base import Model
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    name    = models.CharField(max_length=50)
    email   = models.EmailField(max_length=254)
    age     = models.IntegerField()
    bio     = models.TextField(blank = True, default='I am the BOSS')

    def get_absolute_url(self):
        # 1st parameter is name from urls.py path(name='')
        # 2nd parameter is var from urls.py path('xyz/<type:var>')
        return reverse("person-detail", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("person-update", kwargs={'id': self.id})
    
    