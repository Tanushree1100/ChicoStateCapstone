# Generated by Django 5.0 on 2023-12-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
    ]