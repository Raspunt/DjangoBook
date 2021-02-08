from django.shortcuts import render
from . models import *


def WelcomePage(request):
    return render(request,"Polls/index.html") 


def BooksPage(request):
    books = Books.objects.all()
    return render(request,"Polls/BooksPage.html",context = {'books':books})
