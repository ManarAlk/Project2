
from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Book, Author, Category


@register(Book)
class MaterialBookAdmin(ModelAdmin):
    icon_name = 'book'

    list_display = (
        'title',
        'author',
        'category',
        'isbn',
        'available_copies',
    )

    search_fields = ('title', 'isbn')

    list_filter = (
        'author',
        'category',
        'published_date',
    )


@register(Author)
class MaterialAuthorAdmin(ModelAdmin):
    icon_name = 'person'

    list_display = ('name', 'birth_date')
    search_fields = ('name',)


@register(Category)
class MaterialCategoryAdmin(ModelAdmin):
    icon_name = 'category'

    list_display = ('name',)
    search_fields = ('name',)
