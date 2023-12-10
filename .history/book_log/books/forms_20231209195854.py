# forms.py
from django import forms
from .models import Book, Genre, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'publication_date']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['genres'] = forms.ModelMultipleChoiceField(
            queryset=Genre.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True
        )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'content', 'expectations', 'engaging_plot', 'connection_characters', 'enjoyed_writing', 'confusing_elements', 'themes_resonated', 'unexpected_twists', 'lasting_impression', 'recommendation', 'influence_on_thoughts', 'review_text']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'

        # Set choices for yes/no
        YES_NO_CHOICES = [('yes', 'Yes'), ('no', 'No')]

        # Modify each field to use RadioSelect with yes/no choices
        for field_name in self.fields:
            if field_name not in ['author', 'rating', 'content', 'review_text']:
                self.fields[field_name].widget = forms.RadioSelect(choices=YES_NO_CHOICES)
