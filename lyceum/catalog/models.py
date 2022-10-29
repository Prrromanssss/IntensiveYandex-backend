from django.db import models
from django.core.validators import MinValueValidator as MinValValidator

from .validators import validate_amazing


class CommonFieldsNameIsPublished(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name='Название',
                            help_text='''This attribute keeps
                            the name of the entry''',
                            )
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано',
                                       help_text='''This attribute keeps
                                       information whether the entry
                                       has been published''',
                                       )

    def __str__(self):
        return f'{self.__class__.name}({self.name})'


class CommonFieldsSlug(models.Model):
    slug = models.SlugField(unique=True, max_length=200,
                            verbose_name='Адрес',
                            help_text='''This attribute keeps
                            the url of the entry''',
                            )


class Item(CommonFieldsNameIsPublished):
    text = models.TextField(validators=[validate_amazing, ],
                            verbose_name='Описание',
                            help_text='''This attribute keeps
                            the description of the item''',
                            )
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 help_text='''This attribute keeps
                                 the category of the item''',
                                 )
    tags = models.ManyToManyField('Tag',
                                  on_delete=models.CASCADE,
                                  verbose_name='Тэг',
                                  help_text='''This attribute keeps
                                  the tags that belong to item'''
                                  )


class Tag(CommonFieldsNameIsPublished, CommonFieldsSlug):
    pass


class Category(CommonFieldsNameIsPublished, CommonFieldsSlug):
    weight = models.PositiveSmallIntegerField(default=100,
                                              validators=[MinValValidator(1)],
                                              verbose_name='Вес',
                                              help_text='''This attribute keeps
                                              the weight of the category''',
                                              )


'''
Виды удалений:
    SET_DEFAULT, DO_NOTHING, RESTRICT, PROTECT, CASCADE, SET_NULL
Виды отношений таблиц:
    одно к одному
    одно ко многим
    многие ко многим
'''


'''
CI/CD
setup.cfg
per-file-ignores = */migrations/, *settings.py:E501'''
