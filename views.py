from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
#from .models import User_Info,Expense_Category

def Home_Logs(request): 
    return render(request,"Home.html")

def AddExpenses(request):
    return render(request,"AddExpense.html")

def update(request):
    Username=request.POST["P1"]
    Breakfast=request.POST["P2"]
    Trip=request.POST["P3"]
    Hangout=request.POST["P4"]
    d=ExpenseCategory(Username=Username1,Breakfast= Breakfast1,Trip=Trip1,Hangout=Hangout1)
    d.save()
    return HttpResponse(request,"Home.html")
