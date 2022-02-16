from email.mime import image
from django.db import models

# Create your models here.


class Anime(models.Model):
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass
