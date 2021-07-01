from django.contrib import admin

from .models import Author, Book, Publisher, Store


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "age"]


class BookInlineModelAdmin(admin.TabularInline):
    model = Book
    extra = 5


@admin.register(Publisher)
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [BookInlineModelAdmin]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["name", "pages", "price", "rating", "publisher", "pubdate"]
    date_hierarchy = "pubdate"
    filter_vertical = ["authors"]
    search_fields = ["name"]


@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    filter_vertical = ["books"]
