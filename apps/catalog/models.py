from django.db import models
from django.urls import reverse

import uuid


class Genre(models.Model):
    """
    This model representing book genre
    and this book it is Book model below
    """
    name = models.CharField(max_length=255, verbose_name='genre_name', help_text='Genre of book')

    def __str__(self):
        """
        this method representing genre and return its name
        """
        return self.name


class Book(models.Model):
    """
    This model representing book (as abstract)
    more info you can get from another models
    """
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='You can enter a bref '
                                                          'description you book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 chars for ISBN')

    # linked fields
    genre = models.ManyToManyField(Genre, help_text='Select genre')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        this method representing book and return book`s title
        """
        return self.title

    # Methods for displaying fields to admin panel
    def display_genre(self):
        """
        Genre has m2m link, => one book has many genres
        therefor we have to all genres and make up genres list
        """
        return ' | '.join([gr.name for gr in self.genre.all()])

    def display_author(self):
        """
        return only last name of book (for admin panel)
        """
        return self.author.last_name

    # Titles to admin panel to displaying fields
    display_genre.short_description = 'Genre of book'
    display_author.short_description = 'Author of book'

    def get_absolute_url(self):
        """
        returns the url to access to particular book instance
        """
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    This model representing specific copy of book
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    BOOK_STATUS = (
        ('n', 'Not defined'),
        ('a', 'Available'),
        ('u', 'Already taken'),
    )
    status = models.CharField(max_length=1, choices=BOOK_STATUS, default='n')

    # linked fields
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s "%s"' % (self.id, self.book.title)


class Author(models.Model):
    """
    This model representing book`s author
    P.S. one book can have only one author (in this case)
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_path(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Language(models.Model):
    """
    This model representing language of instance`s book
    """
    name = models.CharField(max_length=50, help_text="Enter original lang")

    def __str__(self):
        return self.name
