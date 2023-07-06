"""
Views for the CRUD_Operation app.
"""

from rest_framework import viewsets
from CRUD_Operation.models import Book
from CRUD_Operation.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    Viewset for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
