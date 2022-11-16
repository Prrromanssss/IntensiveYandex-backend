from django.test import Client, TestCase
from django.urls import reverse


class StaticUrlTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get(reverse('about:description'))
        self.assertEqual(response.status_code, 200)
