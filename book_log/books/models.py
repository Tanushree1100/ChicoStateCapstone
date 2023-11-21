
# Create your models here.
# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
