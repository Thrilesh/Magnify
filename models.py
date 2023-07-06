"""
Module: models.py
Defines the database models for the CRUD_Operation app.
"""

from django.db import models

class BookManager(models.Manager):
    pass

class Book(models.Model):
    """
    Represents a book in the database.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        publication_date (date): The publication date of the book.
    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    objects = BookManager()
