from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from reviews.models import Title, Genre, Category
from .serializers import GenreSerializer, TitleSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    search_fields = ('name',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)



