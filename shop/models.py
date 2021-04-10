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


class Product(models.Model):

   slug = models.SlugField(unique=True)
   vendorСode = models.CharField(max_length=120, verbose_name='Артикул')
   category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
   title = models.CharField(max_length=120, verbose_name='Имя товара')
   description = models.TextField()
   prise1 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='цена(если 2 объема, цена за меньший)')
   img = models.ImageField(default='default.png', upload_to='goods_img')

   class Meta:
       verbose_name = '0Весь ассортимент'
       verbose_name_plural = '0Весь ассортимент'


   def __str__(self):
       return self.title

   def get_absolute_url(self):
       return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})





class ProductSet(Product):

    volumeTrue = models.BooleanField(name='2_volume', verbose_name='Наличие 2ух объемов', default=True)
    volume1 = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True, verbose_name='объем(меньший)')
    volume2 = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True, verbose_name='объем(больший)')
    prise2 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='цена за больший объем')

    class Meta:
        verbose_name = 'Наборы'
        verbose_name_plural = 'Наборы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})







class ProductBestsellers(Product):

    volumeTrue = models.BooleanField(name='2_volume', verbose_name='Наличие 2ух объемов', default=True)
    volume1 = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True, verbose_name='объем(меньший)')
    volume2 = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True, verbose_name='объем(больший)')
    prise2 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='цена за больший объем')
    aromat = models.CharField(max_length=120, verbose_name='аромат')

    class Meta:
        verbose_name = 'Бестселлеры'
        verbose_name_plural = 'Бестселлеры'

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})





class Basket(models.Model):
    session_key = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    quantity = models.IntegerField(default=1)
    article_date = models.DateTimeField(default=datetime.datetime.now())