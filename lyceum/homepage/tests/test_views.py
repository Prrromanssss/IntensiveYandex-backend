from django.test import Client, TestCase
from django.urls import reverse


class TaskPagesTests(TestCase):
    def test_home_page_shown_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
