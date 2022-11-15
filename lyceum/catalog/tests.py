from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from .models import Category, Item, Preview, Tag


class DynamicUrlTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )
        for i in range(101):
            Item.objects.create(
                name=f'Test item {i}',
                text='превосходно',
                category=cls.category,
            )

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
                '1',
                '95',
                '10',
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


class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )
        Item.objects.create(
            name='Test item 1',
            text='превосходно',
            category=cls.category,
        )

    def test_catalog_shown_correct_context(self):
        with self.subTest(
            'Context "items" must be passed - "catalog:item_list"'
        ):
            response = Client().get(reverse('catalog:item_list'))
            self.assertIn('items', response.context)

        with self.subTest(
            'Context "item" must be passed - "catalog:item_detail"'
        ):
            response = Client().get(reverse(
                'catalog:item_detail',
                args=[1])
            )
            self.assertIn('item', response.context)
