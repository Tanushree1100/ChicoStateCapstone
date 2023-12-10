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
            'expectations': forms.RadioSelect(attrs={'class': 'radio'}),
            'engaging_plot': forms.RadioSelect(attrs={'class': 'radio'}),
            'connection_characters': forms.RadioSelect(attrs={'class': 'radio'}),
            'enjoyed_writing': forms.RadioSelect(attrs={'class': 'radio'}),
            'confusing_elements': forms.RadioSelect(attrs={'class': 'radio'}),
            'themes_resonated': forms.RadioSelect(attrs={'class': 'radio'}),
            'unexpected_twists': forms.RadioSelect(attrs={'class': 'radio'}),
            'lasting_impression': forms.RadioSelect(attrs={'class': 'radio'}),
            'recommendation': forms.RadioSelect(attrs={'class': 'radio'}),
            'influence_on_thoughts': forms.RadioSelect(attrs={'class': 'radio'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['expectations'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['engaging_plot'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['connection_characters'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['enjoyed_writing'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['confusing_elements'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['themes_resonated'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['unexpected_twists'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['lasting_impression'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['recommendation'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
        self.fields['influence_on_thoughts'].widget.choices = [('yes', 'Yes'), ('no', 'No')]
