from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category', )
    search_fields = ('name', 'description',)