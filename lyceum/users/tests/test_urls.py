from django.test import Client, TestCase
from django.urls import reverse

from ..models import CustomUser


class StaticUrlTests(TestCase):
    def test_registration_endpoints(self):
        # 'password_reset_confirm',
        endpoints = {
            200: [
                'login',
                'logout',
                'password_reset',
                'password_reset_complete',
                'password_reset_done',
                'sign_up',
            ],
            302: [
                'password_change_done',
                'password_change',
            ],
        }

        for url in endpoints[200]:
            with self.subTest(f'Succes url - {url}'):
                response = Client().get(reverse(f'users:{url}'))
                self.assertEqual(response.status_code, 200)

    def test_users_endpoints(self):
        endpoints = {
            200: [
                'user_list',
            ],
            302: [
                'profile',
            ]

        }
        for url in endpoints[200]:
            with self.subTest(f'Succes url - {url}'):
                response = Client().get(reverse(f'users:{url}'))
                self.assertEqual(response.status_code, 200)


class DynamicUrlTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for i in range(101):
            cls.user = CustomUser.objects.create(
                email=f'user{i}@mail.ru',
                password='bhunji78*',
            )

    def test_(self):
        endpoints = {
            200: [
                '1',
                '95',
                '10',
            ],
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
        }
        for item in endpoints[404]:
            with self.subTest('Do not match regex - "users:users_detail"'):
                response = Client().get(f'/users/{item}')
                self.assertEqual(response.status_code, 404)

        for item in endpoints[200]:
            with self.subTest('Succes Urls - "users:user_detail"'):
                response = Client().get(
                    reverse('users:user_detail',
                            args=[int(item)])
                )
                self.assertEqual(response.status_code, 200)
