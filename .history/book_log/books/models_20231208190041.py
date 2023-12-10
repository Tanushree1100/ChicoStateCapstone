# models.py

from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        # Add more genres as needed
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    publication_date = models.DateField()
    finished_reading = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# models.py

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True)  # Allow null
    author = models.CharField(max_length=255, default='Anonymous')
    rating = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.author}'s review for {self.book.title}"
