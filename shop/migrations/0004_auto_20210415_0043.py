# Generated by Django 3.1.7 on 2021-04-14 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210415_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 0, 43, 49, 605426)),
        ),
    ]
