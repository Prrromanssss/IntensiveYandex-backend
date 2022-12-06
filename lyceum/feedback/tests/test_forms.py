from django.test import Client, TestCase
from django.urls import reverse
from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_text_label(self):
        text_label = self.form.fields['text'].label
        self.assertEqual(text_label, 'Фидбэк')

    def test_name_label(self):
        name_label = self.form.fields['name'].label
        self.assertEqual(name_label, 'Имя')

    def test_mail_label(self):
        mail_label = self.form.fields['mail'].label
        self.assertEqual(mail_label, 'Почта')

    def test_mail_help_text(self):
        mail_help_text = self.form.fields['mail'].help_text
        self.assertEqual(mail_help_text, 'Максимум 254 символа')

    def test_name_help_text(self):
        name_help_text = self.form.fields['name'].help_text
        self.assertEqual(name_help_text, 'Максимум 150 символов')

    def test_create_task(self):
        feedback_count = Feedback.objects.count()

        form_data = {
            'text': 'Тест',
            'name': 'Иванов Иван',
            'mail': '1@example.com',
        }

        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True,
        )

        self.assertRedirects(response, reverse('feedback:feedback'))

        self.assertEqual(Feedback.objects.count(), feedback_count + 1)

        self.assertTrue(
            Feedback.objects.filter(
                text='Тест',
                name='Иванов Иван',
                mail='1@example.com',
            ).exists()
        )
