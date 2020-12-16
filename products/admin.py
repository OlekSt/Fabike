from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'frame', 
        'name',
        'fork',
        'weight',
        'weight_alloy',
        'weight_carbon',
        'price',
        'price_alloy',
        'price_carbon'
        'product_image01',
    )

    ordering = ('frame',)

# Register your models here.
admin.site.register(Product, ProductAdmin)
