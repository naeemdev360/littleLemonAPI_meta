# Generated by Django 4.1.5 on 2023-01-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0002_book'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['price'], name='BookListAPI_price_779a55_idx'),
        ),
    ]
