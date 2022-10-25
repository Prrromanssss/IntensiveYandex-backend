from django.test import Client, TestCase


class DynamicUrlTests(TestCase):
    def test_catalog_endpoints(self):
        endpoints = {404: [
                           '-1', '0', '00', '01', '001',
                           '003456', '00str', '_', '_01',
                           '_45678', '123_456', '123_',
                           'str', 'str123', '123str',
                           '123str456', '1.0', '1.123',
                           ],
                     200: [
                          '123', '100', '1',
                    ]}

        for item in endpoints[404]:
            with self.subTest(f'Do not match regex - /catalog/{item}/'):
                response = Client().get(f'/catalog/{item}/')
                self.assertEqual(response.status_code, 404)

        for item in endpoints[200]:
            with self.subTest(f'Succes Urls - /catalog/{item}/'):
                response = Client().get(f'/catalog/{item}/')
                self.assertEqual(response.status_code, 200)


class StaticUrlTests(TestCase):
    def test_catalog_init(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)
