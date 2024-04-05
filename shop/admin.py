from django.contrib import admin

# Register your models here.
from .models import * #Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','is_active')
    list_filter = ('category','is_active')
    search_fields = ('name','description')