from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from .models import Category, Item, Tag


class DynamicUrlTests(TestCase):
    def test_catalog_endpoints(self):
        endpoints = {
            404: [
                '-1',
                '0',
                '00',
                '01',
                '001',
                '003456',
                '00str',
                '_',
                '_01',
                '_45678',
                '123_456',
                '123_',
                'str',
                'str123',
                '123str',
                '123str456',
                '1.0',
                '1.123',
            ],
            200: [
                '123',
                '100',
                '1',
            ],
        }

        for item in endpoints[404]:
            with self.subTest(f'Do not match regex - /catalog/{item}/'):
                response = Client().get(f'/catalog/{item}/')
                self.assertEqual(response.status_code, 404)

        for item in endpoints[200]:
            with self.subTest(f'Success Urls - /catalog/{item}/'):
                response = Client().get(f'/catalog/{item}/')
                self.assertEqual(response.status_code, 200)


class StaticUrlTests(TestCase):
    def test_catalog_init(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)


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

    def test_without_needed_words(self):
        item_count = Item.objects.count()
        text_endpoints = ['какая-то бессмыслица',
                          'нероскошно',
                          'превосходность',
                          ]
        for text in text_endpoints:
            with self.assertRaises(ValidationError):
                self.item = Item(name='товар номер 1', category=self.category,
                                 text=text)
                self.item.full_clean()
                self.item.save()
                self.item.tags.add(self.tag)

            self.assertEqual(Item.objects.count(), item_count)

    def test_with_needed_words(self):
        item_count = Item.objects.count()
        text_endpoints = [
            'превосходно в нем все',
            'роскошно в нем все',
            'это роскошно и превосходно',
        ]
        for ind, text in enumerate(text_endpoints, start=1):
            with self.subTest(f'The model Item with such text must be created'
                              f' - "{text}"'):
                self.item = Item(
                    name='тестовый товар',
                    category=self.category,
                    text=text,
                )
                self.item.full_clean()
                self.item.save()
                self.item.tags.add(self.tag)

                self.assertEqual(Item.objects.count(),
                                 item_count + ind)
