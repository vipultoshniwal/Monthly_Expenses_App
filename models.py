# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from  MonthlyExpensesApp views

class ExpenseType(models.Model):
    username = models.IntegerField(max_length=50)
    Breakfast = models.IntegerField(max_length=50)
    Trip = models.IntegerField(max_length=50)
    Hangout = models.IntegerField(max_length=50)
