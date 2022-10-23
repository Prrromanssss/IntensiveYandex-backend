from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_negative_endpoins(self):
        response = Client().get('/catalog/-1')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/0')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/str')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/1str')
        self.assertEqual(response.status_code, 404)

    def test_static_endpoints(self):
        response = Client().get('/catalog/123')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/100')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)
