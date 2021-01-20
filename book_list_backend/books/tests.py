from django.core.management import call_command
from django.test import TestCase

from ratings.models import Rating
from .models import Book, Author, Genre


class LoadBooksCommandTests(TestCase):
    @staticmethod
    def call_command(*args, **kwargs):
        ratings_file = kwargs.pop('ratings_file', None) or 'tests/ratings_test.csv'
        call_command(
            'load_books_data',
            books_file='tests/books_test.csv',
            ratings_file=ratings_file,
            *args,
            **kwargs,
        )

    def test_simple_run(self):
        self.assertEqual(0, Book.objects.count())
        self.assertEqual(0, Rating.objects.count())
        self.call_command()
        self.assertEqual(1, Book.objects.count())
        self.assertEqual(1, Rating.objects.count())

    def test_missing_book_in_rating(self):
        self.call_command(ratings_file='tests/ratings_missing_book.csv')
        self.assertEqual(1, Book.objects.count())
        self.assertEqual(0, Rating.objects.count())

    def test_update_existing_book(self):
        author = Author.objects.create(name='test')
        genre = Genre.objects.create(name='test')
        Book.objects.create(isbn='1111111111', author=author, genre=genre)
        self.assertEqual(1, Book.objects.count())

        self.call_command()

        self.assertEqual(1, Book.objects.count())
        book = Book.objects.get(isbn='1111111111')
        self.assertEqual(book.genre.name, 'Kryminał')
        self.assertEqual(book.author.name, 'Alicja Sinicka')

    def test_multiple_run(self):
        author = Author.objects.create(name='test')
        genre = Genre.objects.create(name='test')
        book = Book.objects.create(isbn='1111111111', author=author, genre=genre)
        Rating.objects.create(book=book, rate=1)

        self.assertEqual(1, Book.objects.count())
        self.assertEqual(1, Rating.objects.count())

        self.call_command()

        self.assertEqual(1, Book.objects.count())
        self.assertEqual(2, Rating.objects.count())

        self.call_command()

        self.assertEqual(1, Book.objects.count())
        self.assertEqual(3, Rating.objects.count())

    def test_skip_books_arg(self):
        self.call_command(skip_books=True)
        self.assertEqual(0, Book.objects.count())
        self.assertEqual(0, Rating.objects.count())

    def test_skip_ratings_arg(self):
        self.call_command(skip_ratings=True)
        self.assertEqual(1, Book.objects.count())
        self.assertEqual(0, Rating.objects.count())

    def test_skip_ratings_and_books_arg(self):
        self.call_command(
            skip_ratings=True,
            skip_books=True,
        )
        self.assertEqual(0, Book.objects.count())
        self.assertEqual(0, Rating.objects.count())
