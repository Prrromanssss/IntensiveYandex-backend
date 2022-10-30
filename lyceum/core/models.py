from django.db import models


class CommonFieldsNameIsPublished(models.Model):
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано',
                                       )
    name = models.CharField(max_length=150,
                            verbose_name='Название',
                            help_text='''максимум 150 символов''',
                            )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


class CommonFieldsSlugNameIsPublished(CommonFieldsNameIsPublished):
    slug = models.SlugField(unique=True, max_length=200,
                            verbose_name='Адрес',
                            help_text='''Только slug-значения,
                             максимум 200 символов''',
                            )

    class Meta:
        abstract = True
