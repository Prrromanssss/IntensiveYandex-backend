from django.db import models
from django.db.models import Prefetch


class ItemManager(models.Manager):
    def published(self):
        from .models import Tag
        return (
            self.get_queryset()
            .select_related('category', 'mainimage')
            .filter(
                is_published=True,
                category__is_published=True
            )
            .prefetch_related(
                Prefetch(
                    'tags', queryset=Tag.objects.published()
                )
            )
            .only(
                'name',
                'text',
                'category__name',
                'mainimage__image',
            )
        )


class TagManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .only('name')
        )
