from django.contrib import admin

from .models import Book, Author, Genre


class BookAdmin(admin.ModelAdmin):
    fields = ['isbn', 'title', 'author', 'genre']


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name']


class GenreAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, AuthorAdmin)
