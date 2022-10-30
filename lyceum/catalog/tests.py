from django.test import Client, TestCase
from django.core.exceptions import ValidationError

from .models import Item, Tag, Category


class DynamicUrlTests(TestCase):
    def test_catalog_endpoints(self):
        endpoints = {404: ['-1', '0', '00', '01', '001',
                           '003456', '00str', '_', '_01',
                           '_45678', '123_456', '123_',
                           'str', 'str123', '123str',
                           '123str456', '1.0', '1.123',
                           ],
                     200: ['123', '100', '1',
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
        cls.category = Category.objects.create(name='Тестовая категория',
                                               slug='test-category-slug',)
        cls.tag = Tag.objects.create(name='Тестовая тэг',
                                     slug='test-tag-slug',)

    def test_unable_create_one_letter(self):
        item_count = Item.objects.count()
        try:
            self.item = Item(name='test item', category=self.category,
                             text='test desc')
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
        except ValidationError:
            pass

        self.assertEqual(Item.objects.count(), item_count)

    def test_able_create_one_letter(self):
        item_count = Item.objects.count()
        try:
            self.item = Item(name='test item', category=self.category,
                             text='test превосходно')
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
        except ValidationError:
            pass

        self.assertEqual(Item.objects.count(), item_count + 1)
