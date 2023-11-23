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
