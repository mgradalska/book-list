import csv
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand

from books.models import Book, Genre, Author
from ratings.models import Rating


logger = logging.getLogger(__name__)


class CsvReader:
    FILES_DIR = './books/management/files'

    def __init__(self, filename):
        self._file_path = f'{self.FILES_DIR}/{filename}'

    def read_rows(self):
        with open(self._file_path) as file:
            rows = csv.reader(file, delimiter=';')
            CsvReader._skip_header(rows)
            return list(rows)

    @staticmethod
    def _skip_header(rows):
        next(rows)


class BookReader:
    def __init__(self, filename):
        self._filename = filename

    def load_books(self):
        rows = CsvReader(self._filename).read_rows()
        for row in rows:
            BookReader._create_or_update_book(row[0], row[1], row[2], row[3])

    @staticmethod
    def _create_or_update_book(isbn, title, author, genre):
        genre, _ = Genre.objects.get_or_create(name=genre)
        author, _ = Author.objects.get_or_create(name=author)
        try:
            book = Book.objects.get(isbn=isbn)
            book.title = title
            book.genre = genre
            book.author = author
            book.save()
            logger.info(f'Book {isbn} updated.')
        except ObjectDoesNotExist:
            Book.objects.create(isbn=isbn, author=author, genre=genre, title=title)
            logger.info(f'Book {isbn} created.')


class RatingReader:
    def __init__(self, filename):
        self._filename = filename

    def load_ratings(self):
        rows = CsvReader(self._filename).read_rows()
        for row in rows:
            RatingReader._create_or_update_rating(row[0], row[1], row[2])

    @staticmethod
    def _create_or_update_rating(isbn, rate, description):
        try:
            book = Book.objects.get(isbn=isbn)
            Rating.objects.create(book=book, rate=rate, description=description)
            logger.info(f'Rating for book {isbn} added.')
        except ObjectDoesNotExist:
            logger.error(F'Book with given ISBN ({isbn}) does not exist.')


class Command(BaseCommand):
    help = 'Loads books and ratings data from CSV files places in ./files directory.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--books-file',
            type=str,
            help='Books filename, default books.csv'
        )
        parser.add_argument(
            '--ratings-file',
            type=str,
            help='Ratings filename, default ratings.csv'
        )
        parser.add_argument(
            '--skip-books',
            action='store_true',
            help='Skip loading books',
        )
        parser.add_argument(
            '--skip-ratings',
            action='store_true',
            help='Skip loading ratings',
        )

    def handle(self, *args, **options):
        books_file = options['books_file'] or 'books.csv'
        ratings_file = options['ratings_file'] or 'ratings.csv'
        skip_books = options['skip_books']
        skip_ratings = options['skip_ratings']
        book_reader = BookReader(books_file)
        rating_reader = RatingReader(ratings_file)
        if not skip_books:
            book_reader.load_books()
        if not skip_ratings:
            rating_reader.load_ratings()
