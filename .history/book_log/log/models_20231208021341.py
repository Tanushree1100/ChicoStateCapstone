import json
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.TextField(blank=True)

    def set_authors(self, value):
        self.authors = json.dumps(value)

    def get_authors(self):
        return json.loads(self.authors) if self.authors else []

    def __str__(self):
        return self.title
