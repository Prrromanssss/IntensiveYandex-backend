from core.models import (ImageBaseModel, IsPublishedBaseModel,
                         IsPublishedSlugBaseModel)
from django.db import models

from .validators import validate_amazing


class Item(IsPublishedBaseModel):
    name = models.CharField(
        'название',
        max_length=150,
        help_text='Максимум 150 символов',
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='категория',
        on_delete=models.CASCADE,
        help_text='Выберите категорию',
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='тег',
    )
    text = models.TextField(
        'описание',
        help_text='Описание должно содержать слова "роскошно" и "превосходно"',
        validators=[
            validate_amazing('превосходно', 'роскошно'),
        ],
    )
    preview = models.OneToOneField(
        'Preview',
        verbose_name='превью',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'


class Tag(IsPublishedSlugBaseModel):
    name = models.CharField(
        'название',
        max_length=150,
        unique=True,
        help_text='Максимум 150 символов',
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Category(IsPublishedSlugBaseModel):
    name = models.CharField(
        'название',
        max_length=150,
        unique=True,
        help_text='Максимум 150 символов',
    )
    weight = models.PositiveSmallIntegerField(
        'вес',
        default=100,
        help_text='Максимум 32767',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Preview(ImageBaseModel):
    name = models.CharField(
        'название',
        max_length=150,
        unique=True,
        help_text='Максимум 150 символов',
    )

    class Meta:
        verbose_name = 'превью'
        verbose_name_plural = 'превью'

    def __str__(self):
        return self.name


class Gallery(ImageBaseModel):
    name = models.CharField(
        'название',
        max_length=150,
        unique=True,
        help_text='Максимум 150 символов',
    )
    item = models.ForeignKey(
        'Item',
        verbose_name='товар',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фотогалерея товара'

    def __str__(self):
        return self.name
