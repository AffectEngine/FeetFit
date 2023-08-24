from django.contrib import admin
from .models import FoodCategory, FoodItem


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'image']


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'price', 'is_on_sale', 'sale_price', 'image']
	list_filter = ['category', 'is_on_sale']
