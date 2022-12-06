from catalog.models import Category, Item
from django.test import Client, TestCase
from django.urls import reverse


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
            with self.subTest('Do not match regex - "catalog:item_detail"'):
                response = Client().get(f'/catalog/{item}')
                self.assertEqual(response.status_code, 404)

        for item in endpoints[200]:
            with self.subTest('Succes Urls - "catalog:item_detail"'):
                response = Client().get(
                    reverse('catalog:item_detail',
                            args=[int(item)])
                )
                self.assertEqual(response.status_code, 200)


class StaticUrlTests(TestCase):
    def test_catalog_list(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertEqual(response.status_code, 200)
