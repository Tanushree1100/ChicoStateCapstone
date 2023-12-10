import json
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
