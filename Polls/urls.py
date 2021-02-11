from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . views import *

urlpatterns = [
    path('Wellcome/',WelcomePage , name = "HomePage"),
    path('Book/',BooksPage, name = "BooksPage"),
    path("Genre/<str:slug>",GenreDetail,name = "GenreDetail"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
