from django.contrib import admin
from . models import *




class BooksAdmin(admin.ModelAdmin):
    filter_horizontal = ('Author',"Genre")
    list_filter = ('Genre',"Author")
    search_fields = ('title',)



class Country_BookAdmin(admin.ModelAdmin):
    list_filterss = ('tutle','country')
    filter_horizontal = ('author','books')


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book,BooksAdmin)
admin.site.register(Country)
admin.site.register(Country_Book,Country_BookAdmin)
