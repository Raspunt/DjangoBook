from django.contrib import admin
from . models import *




class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','Author')



admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Books,BooksAdmin)
