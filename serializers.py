"""
Serializers for the CRUD_Operation app.
"""

from rest_framework import serializers
from CRUD_Operation.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'created_at', 'updated_at']
