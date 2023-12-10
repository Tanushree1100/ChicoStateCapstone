from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.TextField(blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.title

