from django.db import models


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

    class Meta:
        ordering = ['-year']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'year'],
                name='unique_title'),
        ]


class GenreTitle(models.Model):
    genre_id = models.ForeignKey(
        Genre,

        on_delete=models.SET_NULL,
        null=True,
        related_name='genre_title',
    )
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='genre_title',
        verbose_name='Айди произведения'
    )

    class Meta:
        ordering = ['-genre_id']
