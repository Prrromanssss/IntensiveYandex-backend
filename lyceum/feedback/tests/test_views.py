from django.test import Client, TestCase
from django.urls import reverse


class TaskPagesTests(TestCase):
    def test_feedback_shown_correct_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)
