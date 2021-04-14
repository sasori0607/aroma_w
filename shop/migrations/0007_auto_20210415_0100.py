# Generated by Django 3.1.7 on 2021-04-14 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210415_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 1, 0, 25, 92364)),
        ),
        migrations.AlterField(
            model_name='product',
            name='newTrue',
            field=models.BooleanField(default=True, verbose_name='Является ли Новинкой'),
        ),
    ]
