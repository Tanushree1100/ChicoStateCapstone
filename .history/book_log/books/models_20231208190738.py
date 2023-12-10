# models.py

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)  # Use ManyToManyField for genres
    publication_date = models.DateField()
    finished_reading = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True)  # Allow null
    author = models.CharField(max_length=255, default='Anonymous')
    rating = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.author}'s review for {self.book.title}"
