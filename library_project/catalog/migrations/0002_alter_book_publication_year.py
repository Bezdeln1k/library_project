# Generated by Django 5.0.4 on 2024-06-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год публикации'),
        ),
    ]