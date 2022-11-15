from django.test import Client, TestCase
from django.urls import reverse


class StaticUrlTests(TestCase):
    def test_homepage_endpoints(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)


class TaskPagesTests(TestCase):
    def test_home_page_shown_correct_context(self):
        with self.subTest(
            f'Context "items" must be passed - {reverse("homepage:home")}'
        ):
            response = Client().get(reverse('homepage:home'))
            self.assertIn('items', response.context)
