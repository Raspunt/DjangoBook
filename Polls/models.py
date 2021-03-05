from django.db import models
from django.shortcuts import reverse





class Genre(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(null=True , blank=True , max_length = 50,unique=True)


    def get_absolute_url(self):
        return reverse('GenreDetail',kwargs={'slug':self.slug})

    def __str__(self):
        return self.title




class Author(models.Model):
    Name = models.CharField(max_length = 300)
    FaceImg = models.ImageField(blank = True)
    DateBirth = models.DateField(blank = True)




    def __str__(self):
        return self.Name


class Book(models.Model):
    title = models.CharField(max_length = 300)
    Author = models.ManyToManyField(Author,blank = True)
    description = models.TextField(blank = True,db_index = True)
    slug = models.SlugField(null=True,blank = True)
    image  = models.ImageField(blank=True)
    Genre = models.ManyToManyField(Genre,blank = True)




    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length = 300)

    def __str__(self):
        return self.title

class Country_Book(models.Model):
    title   = models.CharField(max_length = 300)
    desc    = models.TextField(blank = True,db_index = True)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    books   = models.ManyToManyField(Book,blank = True)
    author  = models.ManyToManyField(Author,blank = True)

    def __str__(self):
        return self.title
