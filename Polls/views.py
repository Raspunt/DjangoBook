from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from . models import *
from  .forms import BookForm

def WelcomePage(request):
    genres = Genre.objects.all()
    return render(request,"Polls/index.html",context = {"genres":genres})


def BooksPage(request):
    books = Book.objects.all()
    return render(request,"Polls/BooksPage.html",context = {'books':books})


def GenreDetail(request,slug):
    genre = Genre.objects.get(slug = slug)
    books = Book.objects.all()

    genreBook = []
    for book in books :
        genreAll = book.Genre.all()
        for gb in genreAll:
            if str(gb) == genre.title:
                genreBook.append(book.title)

    return render(request, 'Polls/GenreDetail.html',context = {'genre':genre,'genreBook':genreBook})



def getCurrentBookPage(request,BookSlug):
    book =  Book.objects.get(slug=BookSlug)
    # books = Book.objects.all()

    return render(request,"Polls/BookDetail.html",{'book':book})



def DeleteBook(request,BookSlug):
    Book.objects.filter(slug=BookSlug).delete()
    return redirect('/Book')


class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "Polls/BookUpdate.html"
    # fields = ['title','Author','description','slug','image','Genre']
    success_url = '/Book'
