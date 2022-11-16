from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import Category, Item, Preview, Tag


class ModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )
        cls.tag = Tag.objects.create(
            name='Тестовая тэг',
            slug='test-tag-slug',
        )
        cls.preview = Preview.objects.create()

    def test_without_needed_words(self):
        item_count = Item.objects.count()
        text_endpoints = [
            'какая-то бессмыслица',
            'нероскошно',
            'превосходность',
        ]
        for text in text_endpoints:
            Item.objects.all().delete()
            with self.subTest(
                 f'This word must fail validation'
                 f' - "{text}"'
                 ):
                with self.assertRaises(ValidationError):

                    self.item = Item(
                        name='товар номер 1',
                        category=self.category,
                        text=text,
                        preview=self.preview,
                    )
                    self.item.full_clean()
                    self.item.save()
                    self.item.tags.add(self.tag)

                self.assertEqual(Item.objects.count(), item_count)

    def test_with_needed_words(self):
        item_count = Item.objects.count()
        text_endpoints = [
            'превосходно в нем все',
            'роскошно в нем все',
            'это роскошно,превосходно',
            'Это роскошно!',
            'Это превосходно?',

        ]
        for text in text_endpoints:
            Item.objects.all().delete()
            with self.subTest(
                 f'The model Item with such text must be created'
                 f' - "{text}"'
                 ):

                self.item = Item(
                    name='тестовый товар',
                    category=self.category,
                    text=text,
                    preview=self.preview,
                )
                self.item.full_clean()
                self.item.save()
                self.item.tags.add(self.tag)
                self.assertEqual(Item.objects.count(), item_count + 1)
