from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "age"]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["name", "pages", "price", "rating", "pubdate"]
    date_hierarchy = "pubdate"
    filter_vertical = ["authors"]
    search_fields = ["name"]
