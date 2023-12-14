# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Book, Genre, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'publication_date']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['genres'].widget = forms.CheckboxSelectMultiple()
        self.fields['genres'].queryset = Genre.objects.all()
        self.fields['genres'].required = True

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'content', 'expectations', 'engaging_plot', 'connection_characters',
                  'enjoyed_writing', 'confusing_elements', 'themes_resonated', 'unexpected_twists',
                  'lasting_impression', 'recommendation', 'influence_on_thoughts', 'review_text']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'expectations': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'engaging_plot': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'connection_characters': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'enjoyed_writing': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'confusing_elements': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'themes_resonated': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'unexpected_twists': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'lasting_impression': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'recommendation': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
            'influence_on_thoughts': forms.TextInput(attrs={'placeholder': 'Enter your response'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'

    # Add a custom validation for the 'rating' field
    def clean_rating(self):
        rating = self.cleaned_data['rating']

        # Check if the rating is within a specific range (e.g., 1 to 5)
        if not 1 <= rating <= 5:
            raise ValidationError('Rating must be between 1 and 5.')

        return rating
