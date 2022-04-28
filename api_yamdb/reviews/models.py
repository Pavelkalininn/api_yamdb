from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    'user',
    'moderator',
    'admin',
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
        choices=ROLE_CHOICES,
        default='user'
    )
