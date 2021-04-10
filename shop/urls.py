from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('you_basket', views.you_basket.as_view(), name='you_basket'),
    path('basket_minus', views.basket_minus, name='basket_minus'),
    path('basket_adding', views.basket_adding, name='basket_adding'),
    path('basket', views.basket, name='basket'),
    path('',  views.Shop_main.as_view(), name='shop_main'),
    path('<category>/<slug>', views.Shop_detail_page.as_view(), name='shop_detail'),
    path('<slug>', views.Shop_category.as_view(), name='shop_category'),
]