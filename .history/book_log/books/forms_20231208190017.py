# books/forms.py
from django import forms
from .models import Book
from .models import Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # Add a choice for the genre field
        self.fields['genre'] = forms.ChoiceField(choices=Book.GENRE_CHOICES, required=True)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating']  # Remove 'content' from this list
