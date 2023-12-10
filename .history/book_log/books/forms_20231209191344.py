# books/forms.py
from django import forms
from .models import Book, Genre, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'publication_date']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # Modify the genres field to be a CheckboxSelectMultiple
        self.fields['genres'] = forms.ModelMultipleChoiceField(
            queryset=Genre.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True
        )

class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
class ReviewForm(forms.ModelForm):
    # Fields for yes/no questions
    expectations = forms.BooleanField(label='Did the book meet your expectations based on its description or genre?', required=False)
    engaging_plot = forms.BooleanField(label='Did you find the plot engaging and well-paced?', required=False)
    connection_characters = forms.BooleanField(label='Did you feel a strong connection to any of the characters in the book?', required=False)
    enjoyed_writing = forms.BooleanField(label='Was there a particular aspect of the book\'s writing style that you enjoyed?', required=False)
    confusing_elements = forms.BooleanField(label='Did you encounter any elements in the story that you found confusing or unenjoyable?', required=False)
    themes_resonated = forms.BooleanField(label='Were there themes or messages in the book that resonated with you?', required=False)
    unexpected_twists = forms.BooleanField(label='Did the book provide any unexpected twists or surprises?', required=False)
    lasting_impression = forms.BooleanField(label='Did the book leave a lasting impression on you after finishing it?', required=False)
    recommendation = forms.BooleanField(label='Would you recommend this book to others?', required=False)
    influence_on_thoughts = forms.BooleanField(label='Did reading this book influence your thoughts or perspective on certain topics?', required=False)

    # Field for additional comments
    review_text = forms.CharField(label='Additional Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['placeholder'] = 'Your Name'
