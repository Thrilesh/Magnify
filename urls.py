"""
URL configuration for the CRUD_Operation app.
"""

from django.urls import include, path
from rest_framework import routers
from CRUD_Operation.views import BookViewSet

# Create a router and register the viewsets
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
