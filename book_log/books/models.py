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

    expectations = models.CharField(max_length=255, default='')
    engaging_plot = models.CharField(max_length=255, default='')
    connection_characters = models.CharField(max_length=255, default='')
    enjoyed_writing = models.CharField(max_length=255, default='')
    confusing_elements = models.CharField(max_length=255, default='')
    themes_resonated = models.CharField(max_length=255, default='')
    unexpected_twists = models.CharField(max_length=255, default='')
    lasting_impression = models.CharField(max_length=255, default='')
    recommendation = models.CharField(max_length=255, default='')
    influence_on_thoughts = models.CharField(max_length=255, default='')
    review_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.author}'s review for {self.book.title}"
