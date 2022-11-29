from django.contrib.auth.admin import User
from django.test import Client, TestCase
from django.urls import reverse


class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for i in range(101):
            cls.user = User.objects.create(
                username=f'Тестовый юзер {i}',
                password='bhunji78*',
            )

    def test_users_shown_correct_context_user_list(self):
        response = Client().get(reverse('users:user_list'))
        self.assertIn('users', response.context)

    def test_users_shown_correct_context_sign_up(self):
        response = Client().get(reverse('users:sign_up'))
        self.assertIn('form', response.context)

    def test_users_shown_correct_context_user_detail(self):
        response = Client().get(reverse(
            'users:user_detail',
            args=[1])
        )
        self.assertIn('user', response.context)

    def test_users_shown_correct_context_profile(self):
        response = Client().get(reverse('users:profile'))
        self.assertIn('user', response.context)
