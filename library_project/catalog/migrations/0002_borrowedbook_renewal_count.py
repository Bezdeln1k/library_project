# Generated by Django 5.0.4 on 2024-05-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='renewal_count',
            field=models.IntegerField(default=0),
        ),
    ]
