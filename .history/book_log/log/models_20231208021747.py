import json
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.JSONField(blank=True, null=True)

    def set_authors(self, value):
        self.authors = value

    def get_authors(self):
        return self.authors or []

    def __str__(self):
        return self.title
