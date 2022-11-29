from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    birthday = models.DateField(
        'день рождения',
        null=True,
    )

    class Meta:
        verbose_name = 'допольнительное поле'
        verbose_name_plural = 'допольнительные поля'

    def __str__(self):
        return 'День рождения'
