from datetime import date

from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class ContextProcessorTests(TestCase):
    def test_context_contains_birthdays_variable(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('birthdays', response.context)

    def test_context_birthdays_variable_is_correct(self):
        response = Client().get(reverse('homepage:home'))
        users_count = (get_user_model().objects.filter(
            birthday=date.today().strftime('%Y-%m-%d'))
            .only('first_name', 'email')).count()
        self.assertEqual(users_count, response.context['birthdays'].count())
