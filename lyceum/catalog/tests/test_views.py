from django.test import Client, TestCase
from django.urls import reverse

from ..models import Category, Item


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

    def test_catalog_shown_correct_context_item_list(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)

    def test_catalog_shown_correct_context_item_detail(self):
        response = Client().get(reverse(
            'catalog:item_detail',
            args=[1])
        )
        self.assertIn('item', response.context)
