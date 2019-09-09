from django.contrib import admin
from apps.catalog.models import Book, BookInstance, Author, Genre, Language


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('display_author', 'display_genre', 'language')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
