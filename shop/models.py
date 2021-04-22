from django.db import models
from django.urls import reverse
from django.contrib import admin
import datetime


class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120, verbose_name='Название категории')

    class Meta:
        verbose_name = '1Категории'
        verbose_name_plural = '1Категории'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        reverse('shop_category', kwargs={'slug': self.category.slug})


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')


class Product(models.Model):

   slug = models.SlugField(unique=True)
   vendorСode = models.CharField(max_length=120, verbose_name='Артикул')
   category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
   title = models.CharField(max_length=120, verbose_name='Имя товара')
   description = models.TextField(verbose_name='Описание')
   volumeTrue = models.BooleanField(verbose_name='Наличие 2ух объемов', default=True)
   prise1 = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='цена(если 2 объема, цена за меньший)')
   volume1 = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True, verbose_name='объем(меньший), если указан')
   volume2 = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True, verbose_name='объем(больший)')
   prise2 = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True,
                                verbose_name='цена за больший объем')
   img = models.ImageField(default='default.png', upload_to='goods_img',verbose_name='Превью изображение')
   newTrue = models.BooleanField(verbose_name='Является ли Новинкой', default=True)
   bestsellerTrue = models.BooleanField(verbose_name='Является ли Bestsellerом', default=False)
   yulia = models.BooleanField(verbose_name='Юлия рекомендует', default=False)
   darina = models.BooleanField(verbose_name='Дарина рекомендует', default=False)

   # Доп модели
   complect = models.TextField(verbose_name='В комплекте', null=True, blank=True)
   grup_aromat = models.CharField(max_length=120, verbose_name='ГРУППА АРОМАТА', null=True, blank=True)
   top_notes = models.CharField(max_length=120, verbose_name='ВЕРХНИЕ НОТЫ', null=True, blank=True)
   heart_notes = models.CharField(max_length=120, verbose_name='НОТЫ СЕРДЦА', null=True, blank=True)
   base_notes = models.CharField(max_length=120, verbose_name='БАЗОВЫЕ НОТЫ', null=True, blank=True)
   link = models.URLField(verbose_name='Ссылка на видео', null=True, blank=True)




   class Meta:
       verbose_name = '0Весь ассортимент'
       verbose_name_plural = '0Весь ассортимент'


   def __str__(self):
       return self.title

   def get_absolute_url(self):
       return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})



class Basket(models.Model):
    session_key = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    vendorСode = models.CharField(max_length=120, verbose_name='Артикул')
    category = models.CharField(max_length=120, verbose_name='Категория')
    volume = models.IntegerField(default=0, verbose_name="Объем", null=True, blank=True, )
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name="Цена")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    img_url = models.CharField(max_length=120, verbose_name='Ссылка на img')
    article_date = models.DateTimeField(default=datetime.datetime.now())

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})



class Order(models.Model):

    name = models.CharField(max_length=256, verbose_name="ФИО")
    phone = models.CharField(verbose_name="Телефон", max_length=64)
    comment = models.TextField(verbose_name='Коментарий', null=True, blank=True)
    delivery = models.TextField(verbose_name='Доставка')
    products = models.TextField(verbose_name='Заказ')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name



