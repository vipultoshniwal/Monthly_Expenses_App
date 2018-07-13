from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
#from .models import User_Info,Expense_Category

def Home_Logs(request): 
    return render(request,"Home.html")
