from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg


class Validators:
    @staticmethod
    def validate_isbn(isbn):
        isbn_digits = len(str(isbn))
        if isbn_digits != 10 and isbn_digits != 13:
            raise ValidationError(f'Incorrect ISBN value: {isbn}. ISBN must contain 10 or 13 digits.')


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.IntegerField(unique=True, validators=[Validators.validate_isbn])
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    @property
    def avg_rating(self):
        avg = self.ratings.aggregate(Avg('rate')).get('rate__avg')
        return round(avg, 1) if avg else None

    def __str__(self):
        return f'{self.title}, {self.author.name}'
