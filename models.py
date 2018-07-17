
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Expensecategories(models.Model):
    Username = models.CharField(max_length=50)
    Breakfast = models.CharField(max_length=50)
    Trip = models.IntegerField()
    Hangout = models.IntegerField()

    def __str__(self):
         return self.Username,self.Breakfast
