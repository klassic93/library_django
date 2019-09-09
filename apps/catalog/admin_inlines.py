from django.contrib import admin
from apps.catalog.models import BookInstance, Book


class BookInstanceLine(admin.TabularInline):
    model = BookInstance

    # This attr remove extra empty fields (if it equal 0)
    # you can check it using admin/catalog/book/<int:pk/change/
    extra = 0


class BookLine(admin.StackedInline):
    model = Book

    # change title for these fields
    verbose_name_plural = 'Him books'

    # This attr remove extra empty fields (if it equal 0)
    # you can check it using admin/catalog/book/<int:pk/change/
    extra = 0
