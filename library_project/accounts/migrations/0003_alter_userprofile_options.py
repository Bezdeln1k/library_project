# Generated by Django 5.0.4 on 2024-05-03 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_reader_card'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Дополнительные поля профиля пользователя'},
        ),
    ]
