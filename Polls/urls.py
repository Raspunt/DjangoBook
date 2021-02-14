from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . views import *

urlpatterns = [
    path('Wellcome/',WelcomePage , name = "HomePage"),
    path('Book/',BooksPage, name = "BooksPage"),
    path("Genre/<str:slug>",GenreDetail,name = "GenreDetail"),
    path("Book/<slug:BookSlug>",getCurrentBookPage, name = ""),
    path("Book/<slug:BookSlug>/del/",DeleteBook, name = ""),
    path("Book/<int:pk>/update/",UpdateBookView.as_view(), name = ""),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
