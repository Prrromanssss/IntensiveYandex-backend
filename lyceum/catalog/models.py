from catalog.managers import ItemManager, TagManager
from catalog.validators import ValidateAmazing
from ckeditor.fields import RichTextField
from core.models import (ImageBaseModel, IsPublishedBaseModel, SlugBaseModel,
                         UniqueNameBaseModel)
from django.db import models


class Item(IsPublishedBaseModel):
    objects = ItemManager()

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
    text = RichTextField(
        'описание',
        help_text='Описание должно содержать слова "роскошно" и "превосходно"',
        validators=[
            ValidateAmazing('превосходно', 'роскошно'),
        ],
    )

    is_on_main = models.BooleanField(
        'на главной',
        default=False,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'
        ordering = ['name']


class Tag(SlugBaseModel, IsPublishedBaseModel, UniqueNameBaseModel):
    objects = TagManager()

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Category(SlugBaseModel, IsPublishedBaseModel, UniqueNameBaseModel):
    weight = models.PositiveSmallIntegerField(
        'вес',
        default=100,
        help_text='Максимум 32767',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class MainImage(ImageBaseModel):
    item = models.OneToOneField(
        'Item',
        verbose_name='товар',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'


class Gallery(ImageBaseModel):
    item = models.ForeignKey(
        'Item',
        verbose_name='товар',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фотогалерея товара'
