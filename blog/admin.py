from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "views_counter")
    list_filter = ("created_at",)
    search_fields = ("id", "title")
