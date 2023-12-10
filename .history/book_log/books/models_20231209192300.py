# models.py

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    publication_date = models.DateField()
    finished_reading = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True)
    author = models.CharField(max_length=255, default='Anonymous')
    rating = models.IntegerField()
    content = models.TextField()

    # New fields for each question in the review form
    expectations = models.BooleanField(default=False)
    engaging_plot = models.BooleanField(default=False)
    connection_characters = models.BooleanField(default=False)
    enjoyed_writing = models.BooleanField(default=False)
    confusing_elements = models.BooleanField(default=False)
    themes_resonated = models.BooleanField(default=False)
    unexpected_twists = models.BooleanField(default=False)
    lasting_impression = models.BooleanField(default=False)
    recommendation = models.BooleanField(default=False)
    influence_on_thoughts = models.BooleanField(default=False)
    review_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.author}'s review for {self.book.title}"
