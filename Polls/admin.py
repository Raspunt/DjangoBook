from django.contrib import admin
from . models import *




class BooksAdmin(admin.ModelAdmin):
    filter_horizontal = ('Author',"Genre")
    list_filter = ('Genre',"Author")
    search_fields = ('title',)



admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Books,BooksAdmin)
