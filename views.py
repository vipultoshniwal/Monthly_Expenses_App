# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
#from .models import ExpenseCategory

def Home_Logs(request): 
    return render(request,"Home.html")

def AddExpenses(request):
    return render(request,"AddExpense.html")

def update(request):
    Username=request.POST["P1"]
    Breakfast=request.POST["P2"]
    Trip=request.POST["P3"]
    Hangout=request.POST["P4"]
    d=ExpenseCategory(Username=Username,Breakfast= Breakfast,Trip=Trip,Hangout=Hangout)
    d.save()
    return HttpResponse(request,"Home.html")

def Login(request):
    return render(request,"Login.html")

def calculation(request): 
    global total  
    Userid=request.POST["P5"]
    r=ExpenseCategory.objects.get(Userid=userid) 
    Breakfast=r.Breakfast
    Trip=r.Trip
    Hangout=r.Hangout
    total=Breakfast+Trip+Hangout
    P={'Breakfast':Breakfast,'Trip':Trip,'Hangout':Hangout,'total':sum}
    return render(request,Sum.html",{'P':P})

def DivideExpense(request):
    Person=request.GET["P6"]
    SeperateValue=int(total)/int(Persons)
    return render(request,"Seperate.html",{'SeperateValue':SeperateValue})





