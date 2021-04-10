from django.contrib import admin
from .models import *
from django.forms import ModelForm


class OllCheck(admin.ModelAdmin):
    search_fields = ('title', 'slug')
    list_display = ('title', 'slug', 'prise1', 'vendorСode', 'category')
    change_form_template = 'admin.html'



admin.site.register(Product, OllCheck)
admin.site.register(Category)
admin.site.register(Basket)


admin.site.register(ProductBestsellers, OllCheck)
admin.site.register(ProductSet, OllCheck)




