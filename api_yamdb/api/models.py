import datetime

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное название латиницей'
    )


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название жанра')
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное название латиницей'
    )


class Title(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название произведения'
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        verbose_name='Год произведения'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанр')
    description = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Описание произведения'
    )


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Заголовок отзыва'
    )
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        verbose_name='Оценка')

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
