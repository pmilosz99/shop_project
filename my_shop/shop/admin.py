from django.contrib import admin

from .models import Category, Product, Producer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name']

