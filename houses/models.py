from unittest.util import _MAX_LENGTH
from django.db import models

# Description of the shape of the data in the application

# Create your models here.

class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140) # Some text with limit of characters 
    price = models.PositiveIntegerField()
    description = models.TextField() # Longer than CharField
    address = models.CharField(max_length=140)
