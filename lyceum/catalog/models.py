from django.db import models
from django.core.validators import MinLengthValidator as MinLenValidator

from .validators import validate_amazing
from core.models import CommonFieldsNameIsPublished
from core.models import CommonFieldsSlugNameIsPublished


class Item(CommonFieldsNameIsPublished):
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 help_text='''Выберите категорию''',
                                 related_name='items',
                                 )
    tags = models.ManyToManyField('Tag',
                                  verbose_name='Тэг',
                                  help_text='''Удерживайте "Control"
                                   (или "Command" на Mac),
                                   чтобы выбрать несколько значений ''',
                                  related_name='items',
                                  )
    text = models.TextField(validators=[validate_amazing('превосходно',
                                                     'роскошно'),
                                        MinLenValidator(2)],
                            verbose_name='Описание',
                            help_text='''Описание должно быть больше, чем
                             из двух символов и содержать слова "роскошно,
                             превосходно"''',
                            )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(CommonFieldsSlugNameIsPublished):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(CommonFieldsSlugNameIsPublished):
    weight = models.PositiveSmallIntegerField(default=100,
                                              validators=[MinLenValidator(1)],
                                              verbose_name='Вес',
                                              help_text='''Какой-то вес, я хз,
                                               что это''',
                                              )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
