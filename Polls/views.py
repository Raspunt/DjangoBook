from django.shortcuts import render, redirect
from django.views.generic import UpdateView,CreateView
from . models import *
from . forms import BookForm

def WelcomePage(request,genre_id):
    genres = Genre.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()



    genre_id = 0
    sq = request.GET.get('sq')

    if 'genre_id' in request.GET:
        genre_id = request.GET.get('genre_id')

    if genre_id != None:
        if int(genre_id) != 0:
            books = Book.objects.filter(Genre = genre_id)
        elif sq != None:
            books = Book.objects.filter(title__contains=sq)
        else :
            books = Book.objects.all()






    print(books)
    return render(request,"Polls/index.html",context =
    {
    "genres":genres,
    'books':books,
    'authors':authors
    })


def BooksPage(request):
    data = {
    'books':Book.objects.all(),
    'genres':Genre.objects.all(),
    'authors':Author.objects.all(),
    }
    return render(request,"Polls/BooksPage.html",data)


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


# class CreateBookView(CreateView):
#     model = Book
#     form_class = BookForm
#     template_name = "Polls/AddBook.html"
#     success_url = '/Book'



def FilterObjects(request):
    genres = Genre.objects.all()
    authors = Author.objects.all()
    books = Book.objects.all()

    print(f' это строка {request.POST}\n')

    if request.POST:
        auth = request.POST.get('aut')
        genre = request.POST.get('genre')

        if genre != None:
            books = Book.objects.filter(Genre = genre)
        if auth != None:
            books = Book.objects.filter(Author = auth)



    print(f'лул {books}')
    return render(request,"Polls/index.html",{
    'books':books,
    'authors':authors,
    'genres':genres,
    })


def CreateBook(request):
    if request.method == 'POST':

        SaveData = {
        'title':request.POST.get('title'),
        # 'Author':request.POST.getlist('Author'),
        'description':request.POST.get('description'),
        'slug':request.POST.get('slug'),
        'image':request.FILES.get('image'),
        # 'Genre':request.POST.getlist('Genre'),
        }



    book = Book.objects.create(**SaveData)

    for aut in request.POST.getlist('Author'):
        a = Author.objects.get(Name = aut)
        book.Author.add(a)

    for gen in request.POST.getlist('Genre'):
        g = Genre.objects.get(title = gen)
        book.Genre.add(g)



    return redirect('/Book/')
