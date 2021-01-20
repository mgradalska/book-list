from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer


class BookListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    queryset = Book.objects.all()
