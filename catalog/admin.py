from django.contrib import admin

from catalog.models import Product, Category, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "telephone")
    search_fields = ("name", "telephone")
