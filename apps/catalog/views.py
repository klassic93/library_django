from django.shortcuts import render
from django.views import generic
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

    return render(request, 'catalog/index.html', context=req_context)


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.filter(language__name='English')
    template_name = 'catalog/books/index.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['another_data'] = 'These all English book in our library.'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/books/instance.html'
