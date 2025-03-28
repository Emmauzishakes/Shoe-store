from django.contrib import admin
from .models import Product, ProductNew, Cart

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

admin.site.register(ProductNew)

admin.site.register(Cart)