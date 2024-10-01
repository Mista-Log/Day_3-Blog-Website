from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    reff = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    image = models.ImageField(default='', blank=True)

    def __str__(self):
        return self.tittle