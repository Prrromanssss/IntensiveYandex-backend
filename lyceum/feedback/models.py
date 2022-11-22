from django.db import models


class Feedback(models.Model):
    name = models.CharField(
        'имя',
        max_length=150,
        default='',
        help_text='Максимум 150 символов',
    )

    mail = models.EmailField(
        'почта',
        max_length=254,
        default='1@example.com',
        help_text='Максимум 254 символа',
    )
    text = models.TextField(
        'фидбэк',
    )

    created_on = models.DateTimeField(
        'дата написания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'фидбэк'
        verbose_name_plural = 'фидбэки'

    def __str__(self):
        return self.short_text()

    def short_text(self):
        return (
            self.text
            if len(self.text) < 20
            else f'{self.text[:20]}...'
        )

    short_text.short_description = 'описание фидбэка'
