from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Trail(models.Model):
    trail_name=models.CharField(max_length=30)
    difficulty=models.CharField(max_length=2, default='DEFAULT')
    trail_length=models.DecimalField(max_digits=5,decimal_places=2)
    maps_link=models.CharField(max_length=255)
   
    
    
class User(models.Model):
    user_name=models.CharField(max_length=30)
    pass_word=models.CharField(max_length=30)
    email=models.CharField(max_length=320, default='DEFAULT')    