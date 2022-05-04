from django.urls import include, path

from api.views import (CategoryViewSet, GenreViewSet, ReviewViewSet,
                       TitleViewSet)
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'genres', GenreViewSet, basename='genre-list')
router.register(r'titles', TitleViewSet, basename='title-list')
router.register(r'categories', CategoryViewSet, basename='category-list')

router.register(
    r'titles/?P<title_id>\d+/reviews',
    ReviewViewSet,
    basename='review-list'
)

urlpatterns = [
    path('v1/', include(router.urls))
]
