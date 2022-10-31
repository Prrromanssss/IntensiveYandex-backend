from django.db import models


class IsPublishedBaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано',
                                       default=True,
                                       )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


class IsPublishedSlugBaseModel(IsPublishedBaseModel):
    slug = models.SlugField(
        'Slug',
        max_length=200,
        unique=True,
        help_text='Только slug-значения,'
        ' максимум 200 символов',
    )

    class Meta:
        abstract = True
