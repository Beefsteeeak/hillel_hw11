from django.contrib import admin

from .models import Author, Quote


class QuoteInlineModelAdmin(admin.TabularInline):
    model = Quote


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'description']
    inlines = [QuoteInlineModelAdmin]


@admin.register(Quote)
class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ['description', 'author']
