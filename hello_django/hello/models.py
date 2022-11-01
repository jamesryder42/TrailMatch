from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Trail(models.Model):
    trail_name=models.CharField(max_length=30)
    difficulty=models.PositiveIntegerField
    trail_length=models.DecimalField(max_digits=5,decimal_places=2)
    lat=models.DecimalField(max_digits=9,decimal_places=6)
    lon=models.DecimalField(max_digits=9,decimal_places=6)
    maps_link=models.CharField(max_length=200)
    
    
class User(models.Model):
    user_name=models.CharField(max_length=30)
    pass_word=models.CharField(max_length=30)
    