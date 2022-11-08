from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class IsPublishedBaseModel(models.Model):
    is_published = models.BooleanField(
        'опубликовано',
        default=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class IsPublishedSlugBaseModel(IsPublishedBaseModel):
    slug = models.SlugField(
        'slug',
        max_length=200,
        unique=True,
        help_text='Только slug-значения, максимум 200 символов',
    )

    class Meta:
        abstract = True


class ImageBaseModel(models.Model):
    image = models.ImageField(
        'превью товара',
        upload_to='previews/%Y/%m/%d',
        blank=True,
    )

    @property
    def get_img(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}" '
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True
    image_tmb.verbose_name = 'hgfjj'

    class Meta:
        abstract = True
