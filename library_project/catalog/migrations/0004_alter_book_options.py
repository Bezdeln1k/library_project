# Generated by Django 5.0.4 on 2024-06-14 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_book_publication_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'книгу', 'verbose_name_plural': 'Книги'},
        ),
    ]
