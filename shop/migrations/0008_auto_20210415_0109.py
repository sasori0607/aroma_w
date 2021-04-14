# Generated by Django 3.1.7 on 2021-04-14 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210415_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 1, 9, 54, 715945)),
        ),
    ]
