from django.shortcuts import render
from apps.catalog.models import Book, Author, BookInstance


def index(request):
    """
    This main function. It return main page
    and some params for main page
    """
    req_context = {
        'count_books': Book.objects.all().count(),
        'count_authors': Author.objects.all().count(),
        'count_bookinstances': BookInstance.objects.count(),
        'available_books': Book.objects.filter(bookinstance__status='a'),
        'genres': Book.objects.filter(author__last_name__icontains='толстой').count()
    }

    return render(
        request,
        'catalog/index.html',
        context=req_context
    )
