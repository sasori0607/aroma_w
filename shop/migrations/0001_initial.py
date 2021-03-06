# Generated by Django 3.1.7 on 2021-04-21 16:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('vendorСode', models.CharField(max_length=120, verbose_name='Артикул')),
                ('category', models.CharField(max_length=120, verbose_name='Категория')),
                ('volume', models.IntegerField(blank=True, default=0, null=True, verbose_name='Объем')),
                ('price', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=1, verbose_name='Количество')),
                ('img_url', models.CharField(max_length=120, verbose_name='Ссылка на img')),
                ('article_date', models.DateTimeField(default=datetime.datetime(2021, 4, 21, 19, 32, 3, 192905))),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=120, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': '1Категории',
                'verbose_name_plural': '1Категории',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=64, verbose_name='Телефон')),
                ('comment', models.TextField(verbose_name='Коментарий')),
                ('delivery', models.TextField(verbose_name='Доставка')),
                ('products', models.TextField(verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('vendorСode', models.CharField(max_length=120, verbose_name='Артикул')),
                ('title', models.CharField(max_length=120, verbose_name='Имя товара')),
                ('description', models.TextField(verbose_name='Описание')),
                ('volumeTrue', models.BooleanField(default=True, verbose_name='Наличие 2ух объемов')),
                ('prise1', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='цена(если 2 объема, цена за меньший)')),
                ('volume1', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='объем(меньший), если указан')),
                ('volume2', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='объем(больший)')),
                ('prise2', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='цена за больший объем')),
                ('img', models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Превью изображение')),
                ('newTrue', models.BooleanField(default=True, verbose_name='Является ли Новинкой')),
                ('bestsellerTrue', models.BooleanField(default=False, verbose_name='Является ли Bestsellerом')),
                ('yulia', models.BooleanField(default=False, verbose_name='Юлия рекомендует')),
                ('darina', models.BooleanField(default=False, verbose_name='Дарина рекомендует')),
                ('complect', models.TextField(blank=True, null=True, verbose_name='В комплекте')),
                ('grup_aromat', models.CharField(blank=True, max_length=120, null=True, verbose_name='ГРУППА АРОМАТА')),
                ('top_notes', models.CharField(blank=True, max_length=120, null=True, verbose_name='ВЕРХНИЕ НОТЫ')),
                ('heart_notes', models.CharField(blank=True, max_length=120, null=True, verbose_name='НОТЫ СЕРДЦА')),
                ('base_notes', models.CharField(blank=True, max_length=120, null=True, verbose_name='БАЗОВЫЕ НОТЫ')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': '0Весь ассортимент',
                'verbose_name_plural': '0Весь ассортимент',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
        ),
    ]
