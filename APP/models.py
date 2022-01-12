from django.db import models

# Create your models here.
class project(models.Model):
    tile = models.CharField(max_length=100)