# Generated by Django 3.1.7 on 2021-04-21 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210421_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 19, 45, 5, 342642)),
        ),
    ]