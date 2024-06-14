# Generated by Django 5.0.4 on 2024-06-04 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_borrowedbook_is_returned_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='borrowedbook',
            options={'verbose_name': 'Выданная книга', 'verbose_name_plural': 'Выданные книги'},
        ),
        migrations.AddField(
            model_name='book',
            name='inventory_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Инвентарный номер'),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ISBN'),
        ),
    ]
