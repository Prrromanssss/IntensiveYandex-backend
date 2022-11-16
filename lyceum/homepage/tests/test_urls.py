from django.test import Client, TestCase
from django.urls import reverse


class StaticUrlTests(TestCase):
    def test_homepage_endpoints(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)
