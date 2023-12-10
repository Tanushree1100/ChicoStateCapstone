# forms.py
from django import forms
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
            'expectations': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'engaging_plot': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'connection_characters': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'enjoyed_writing': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'confusing_elements': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'themes_resonated': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'unexpected_twists': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'lasting_impression': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'recommendation': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
            'influence_on_thoughts': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'

    def clean_expectations(self):
        return self.cleaned_data['expectations'] == 'yes'

    def clean_engaging_plot(self):
        return self.cleaned_data['engaging_plot'] == 'yes'

    def clean_connection_characters(self):
        return self.cleaned_data['connection_characters'] == 'yes'

    def clean_enjoyed_writing(self):
        return self.cleaned_data['enjoyed_writing'] == 'yes'

    def clean_confusing_elements(self):
        return self.cleaned_data['confusing_elements'] == 'yes'

    def clean_themes_resonated(self):
        return self.cleaned_data['themes_resonated'] == 'yes'

    def clean_unexpected_twists(self):
        return self.cleaned_data['unexpected_twists'] == 'yes'

    def clean_lasting_impression(self):
        return self.cleaned_data['lasting_impression'] == 'yes'

    def clean_recommendation(self):
        return self.cleaned_data['recommendation'] == 'yes'

    def clean_influence_on_thoughts(self):
        return self.cleaned_data['influence_on_thoughts'] == 'yes'
