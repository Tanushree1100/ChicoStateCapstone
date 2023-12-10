# Generated by Django 5.0 on 2023-12-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_review_author_review_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Science Fiction', 'Science Fiction'), ('Mystery', 'Mystery'), ('Fantasy', 'Fantasy')], max_length=100),
        ),
    ]
