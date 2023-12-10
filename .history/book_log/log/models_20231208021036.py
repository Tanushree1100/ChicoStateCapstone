from django.db import models
from django.contrib.postgres.fields import ArrayField

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = ArrayField(models.CharField(max_length=255),blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.title
