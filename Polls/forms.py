from django import forms
from . models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','Author','description','slug','image','Genre')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'Author': forms.SelectMultiple(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'Genre': forms.SelectMultiple(attrs={'class':'form-control'}),
        }
