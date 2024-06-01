# Generated by Django 5.0.4 on 2024-05-03 10:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_borrowedbook_renewal_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='borrowedbook',
            options={'verbose_name': 'Заимствованная книга', 'verbose_name_plural': 'Заимствованные книги'},
        ),
        migrations.RemoveField(
            model_name='borrowedbook',
            name='renewal_requested',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(verbose_name='Год публикации'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='borrowed_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата заимствования'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Читатель'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='renewal_count',
            field=models.IntegerField(default=0, verbose_name='Количество продлений'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='return_date',
            field=models.DateField(verbose_name='Дата возврата'),
        ),
    ]
