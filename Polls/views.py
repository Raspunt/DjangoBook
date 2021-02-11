from django.shortcuts import render
from . models import *


def WelcomePage(request):
    genres = Genre.objects.all()
    return render(request,"Polls/index.html",context = {"genres":genres})


def BooksPage(request):
    books = Books.objects.all()
    return render(request,"Polls/BooksPage.html",context = {'books':books})


def GenreDetail(request,slug):
    genre = Genre.objects.get(slug__iexact = slug)
    books = Book.objects.all()

    genreBook = []
    for book in books :
        genreAll = book.Genre.all()
        for gb in genreAll:
            if str(gb) == genre.title:
                genreBook.append(book.title)

    return render(request, 'Polls/GenreDetail.html',context = {'genre':genre,'genreBook':genreBook})
