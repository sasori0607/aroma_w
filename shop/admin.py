from django.contrib import admin
from .models import *
from django.forms import ModelForm

class GalleryInline(admin.TabularInline):
    model = Gallery

class OllCheck(admin.ModelAdmin):
    inlines = [GalleryInline]
    search_fields = ('title', 'slug')
    list_display = ('title', 'slug', 'prise1', 'vendorСode', 'category')
    change_form_template = 'admin.html'





admin.site.register(Product, OllCheck)
admin.site.register(Category)
admin.site.register(Basket)
#admin.site.register(Some, OllCheck)










