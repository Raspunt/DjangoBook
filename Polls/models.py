from django.db import models





class Genre(models.Model):
    title = models.CharField(max_length = 300)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    Name = models.CharField(max_length = 300)
    FaceImg = models.ImageField(blank=True) 
    DateBirth = models.DateField()
    



    def __str__(self):
        return self.Name
    






class Books(models.Model):
    title = models.CharField(max_length = 300)
    Author = models.ForeignKey(Author,on_delete = models.CASCADE)
    description = models.TextField()
    image  = models.ImageField(blank=True)
    Genre = models.ForeignKey(Genre,on_delete = models.CASCADE)
    
    
    

    def __str__(self):
        return self.title


