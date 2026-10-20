from rest_framework import viewsets
from .models import Book, Author, Category
from .serializers import ( BookSerializer, AuthorSerializer, CategorySerializer,)
from .permissions import IsAdminOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author', 'category').all()

    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

    filterset_fields = ['author', 'category']
    search_fields = ['title']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]