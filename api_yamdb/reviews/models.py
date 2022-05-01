from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

ROLE_CHOICES = (
    'user',
    'moderator',
    'admin',
)
Group.objects.bulk_create([
    Group('user'),
    Group('moderator'),
    Group('admin'),
])
# Добавить разрешения в группы


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

    @property
    def is_admin(self):
        if self.role == 'admin':
            return True
        return False

    @property
    def is_staff(self):
        return self.is_admin or self.is_superuser

    @property
    def is_moderator(self):
        if self.role == 'moderator':
            return True
        return False

    def get_user_permissions(self, obj):
        if self.is_superuser:
            return Permission.objects.all()
        # elif self.is_admin:
        return Permission.objects.filter(group__user=self.role)
        # elif self.is_moderator:
        #     ...
        # elif self.is_anonymous:
        #     ...
        # else:
        #     ...
        # return super().get_user_permissions(obj)

    class Meta:
        permissions = [
            ('can_choose_user_role', 'Can choose the role of user'),
        ]
