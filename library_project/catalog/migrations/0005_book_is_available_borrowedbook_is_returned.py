# Generated by Django 5.0.4 on 2024-05-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_book_options_alter_borrowedbook_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
        migrations.AddField(
            model_name='borrowedbook',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
