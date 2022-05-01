import jwt
from api_yamdb.settings import SECRET_KEY
from django.db import models
from django.contrib.auth.models import AbstractUser  # , Permission, Group
from django.utils.crypto import get_random_string

ROLE_CHOICES = (
    ('USER', 'user'),
    ('MODERATOR', 'moderator'),
    ('ADMIN', 'admin'),
)


class User(AbstractUser):
    username = models.CharField(
        'Никнейм',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        'Почта',
        unique=True,
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Роль',
        max_length=16,
        choices=ROLE_CHOICES,
        default='user'
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=64,
        default=get_random_string(length=64)
    )

    REQUIRED_FIELDS = ['email']

    @property
    def is_admin(self):
        if self.role == 'admin':
            return True
        return False

    @property
    def is_moderator(self):
        if self.role == 'moderator':
            return True
        return False

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Генерирует JWT-token, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """

        token = jwt.encode({
            'id': self.pk,
        }, SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Genre(models.Model):
    name = models.TextField(
        'Жанр',
        help_text='Введите жанр'
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        ordering = ['-name']


class Category(models.Model):
    name = models.TextField(
        'Категория',
        help_text='Введите категорию'
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        ordering = ['-name']


class Title(models.Model):
    name = models.TextField(
        'Произведение',
        help_text='Введите произведение'
    )
    year = models.PositiveSmallIntegerField(
        help_text='Введите год издания'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='title',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')

    class Meta:
        ordering = ['-year']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'year'],
                name='unique_title'),
        ]


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
