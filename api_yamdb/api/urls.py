from django.urls import path, include
from rest_framework import routers

from .views import (
    CategoryViewSet,
    TitleViewSet,
    GenreViewSet,
    SignUpView,
    TokenView,
    UserViewSet,
)

router = routers.DefaultRouter()

router.register(r'genres', GenreViewSet, basename='genre-list')
router.register(r'titles', TitleViewSet, basename='title-list')
router.register(r'categories', CategoryViewSet, basename='category-list')
router.register(r'users', UserViewSet)

urlpatterns = [
    path(
        'v1/auth/signup/',
        SignUpView.as_view({'post': 'create'}),
        name='auth-signup'
    ),
    path(
        'v1/auth/token/',
        TokenView.as_view(),
        name='auth-token'
    ),
    path('v1/', include(router.urls)),
]
