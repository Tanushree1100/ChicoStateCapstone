# book_app/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    isbn = models.CharField(max_length=20)
    page_count = models.IntegerField(null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    info_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class ReadingList(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"Reading List for {self.user.username}"
