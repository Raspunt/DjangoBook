from django.urls import path, include , re_path
from django.conf.urls.static import static
from django.conf import settings


from . views import *

urlpatterns = [

    re_path(r'^(?P<genre_id>)$',WelcomePage , name = "HomePage"),
    path('filter/',FilterObjects , name = "FilterObjects"),
    re_path('filterAndSearch/',SearchObjects , name = "SearchObjects"),

    path('Book/',BooksPage, name = "BooksPage"),
    path("Genre/<str:slug>",GenreDetail,name = "GenreDetail"),
    path("Book/<slug:BookSlug>",getCurrentBookPage, name = ""),
    path("Book/<slug:BookSlug>/del/",DeleteBook, name = ""),
    path("Book/<int:pk>/update/",UpdateBookView.as_view(), name = "updateViewUrl"),
    path("Book/create/",CreateBook, name = "createViewUrl")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
