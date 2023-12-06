# models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    finished_reading = models.BooleanField(default=False)  # Add this line

    def __str__(self):
        return self.title


class Review(models.Model):
    # Your fields for the Review model
    content = models.TextField()
    rating = models.IntegerField()

    # Add any other fields as needed

    def __str__(self):
        return self.content  # Or whatever makes sense as a string representation
