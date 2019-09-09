from django.contrib import admin

from apps.catalog.models import Book, BookInstance, Author, Genre, Language
from apps.catalog.admin_inlines import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))

    inlines = [BookLine, ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre', 'language')

    fieldsets = (
        ('Main information', {
            'fields': ('title', 'summary')
        }),
        ('Choose author and language', {
            'fields': (('author', 'language'), )
        }),
        ('Any info', {
            'fields': (('genre', 'isbn'), )
        })
    )

    inlines = [BookInstanceLine, ]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
