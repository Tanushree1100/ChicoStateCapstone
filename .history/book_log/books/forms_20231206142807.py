# books/forms.py
from django import forms
from .models import Book
from .models import Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating']  # Remove 'content' from this list
