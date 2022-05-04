from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_simplejwt.views import TokenViewBase

from reviews.models import Title, Genre, Category, User
from core.custom_authentication import AuthenticationWithoutPassword

from .serializers import (
    GenreSerializer,
    TitleSerializer,
    CategorySerializer,
    SignUpSerializer,
    TokenSerializer,
    UserSerializer
)
from .permissions import AdminOrReadOnly, AdminOnly


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AdminOrReadOnly, ]
    search_fields = ('name',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly, ]
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [AdminOrReadOnly, ]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)


# class AuthView(viewsets.GenericViewSet, TokenViewBase):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)

#     @action(methods=['post'], detail=False)
#     def signup(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         # headers = self.get_success_headers(serializer.data)
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK,
#             # headers=headers
#         )

#     @action(methods=['post'], detail=False)
#     def token(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid()
#         # print(serializer)
#         # headers = self.get_success_headers(serializer.data)
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK,
#             # headers=headers
#         )
#         # serializer = self.serializer_class(data=request.data,
#         #                                    context={'request': request})
#         # serializer.is_valid(raise_exception=True)
#         # user = serializer.validated_data['user']
#         # token, created = Token.objects.get_or_create(user=user)
#         # return Response({
#         #     'token': token.key,
#         #     'user_id': user.pk,
#         #     'email': user.email
#         # })

#     def get_serializer_class(self):
#         if self.action == 'token':
#             return TokenSerializer
#         return SignUpSerializer
class SignUpView(CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers
        )


class TokenView(TokenViewBase):
    permission_classes = (AllowAny,)
    # authentication_classes = (AuthenticationWithoutPassword,)
    serializer_class = TokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AdminOnly,)

    @action(methods=['get', 'patch'], detail=True)
    def me(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    # def get_serializer_class(self):
    #     return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'me':
            return (IsAuthenticated(),)
        return (AdminOnly(),)
