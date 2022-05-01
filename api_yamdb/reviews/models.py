from django.db import models
from django.contrib.auth.models import AbstractUser  # , Permission, Group

ROLE_CHOICES = (
    ('USER', 'user'),
    ('MODERATOR', 'moderator'),
    ('ADMIN', 'admin'),
)


class User(AbstractUser):
    email = models.EmailField(
        'Почта',
        unique=True
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=16,
        choices=ROLE_CHOICES,
        default='user'
    )

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
