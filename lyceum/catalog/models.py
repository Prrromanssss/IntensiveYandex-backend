from ckeditor.fields import RichTextField
from core.models import (ImageBaseModel, IsPublishedBaseModel, SlugBaseModel,
                         UniqueNameBaseModel)
from django.db import models
from django.db.models import Prefetch

from .validators import validate_amazing


class TagManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .only('name')
        )


class ItemManager(models.Manager):
    def published(self, order_by=None, is_on_main=None):
        query_set = (
            self.get_queryset()
            .select_related('category')
            .filter(
                is_published=True,
                category__is_published=True
            )
            .prefetch_related(
                Prefetch(
                    'tags', queryset=Tag.objects.published()
                )
            )
            .only('name', 'text', 'category_id', 'category__name')
        )

        if is_on_main is not None:
            query_set = query_set.filter(is_on_main=is_on_main)

        if order_by is not None:
            query_set = query_set.order_by(order_by)

        return query_set # noqa


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
            validate_amazing('превосходно', 'роскошно'),
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


class Preview(ImageBaseModel):
    item = models.OneToOneField(
        'Item',
        verbose_name='товар',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = 'превью'
        verbose_name_plural = 'превью'


class Gallery(ImageBaseModel):
    item = models.ForeignKey(
        'Item',
        verbose_name='товар',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фотогалерея товара'
