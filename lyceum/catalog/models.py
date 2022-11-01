from core.models import IsPublishedBaseModel, IsPublishedSlugBaseModel
from django.core.validators import MinValueValidator
from django.db import models

from .validators import validate_amazing


class Item(IsPublishedBaseModel):
    name = models.CharField('Название',
                            max_length=150,
                            help_text='Максимум 150 символов',
                            )
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        on_delete=models.CASCADE,
        help_text='Выберите категорию',
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Тег',
    )
    text = models.TextField(
        'Описание',
        help_text='Описание должно содержать слова "роскошно" и "превосходно"',
        validators=[
            validate_amazing('превосходно', 'роскошно'),
        ],
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        default_related_name = 'items'


class Tag(IsPublishedSlugBaseModel):
    name = models.CharField('Название',
                            max_length=150,
                            unique=True,
                            help_text='Максимум 150 символов',
                            )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(IsPublishedSlugBaseModel):
    name = models.CharField('Название',
                            max_length=150,
                            unique=True,
                            help_text='Максимум 150 символов',
                            )
    weight = models.PositiveSmallIntegerField(
        'Вес',
        default=100,
        help_text='Максимум 32767',
        validators=[MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
