from django.urls import path, include
from rest_framework import routers

from api.views import CategoryViewSet, TitleViewSet, GenreViewSet

router = routers.DefaultRouter()

router.register(r'genres', GenreViewSet, basename='genre-list')
router.register(r'titles', TitleViewSet, basename='title-list')
router.register(r'categories', CategoryViewSet, basename='category-list')

urlpatterns = [
    path('v1/', include(router.urls))
]
