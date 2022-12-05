from catalog.models import Item
from django.db import models
from users.models import CustomUser


class Rating(models.Model):
    class Grades(models.IntegerChoices):
        HATE = 1, 'Ненависть'
        DISAFECTION = 2, 'Неприязнь'
        NORMAL = 3, 'Нейтрально'
        ADORATION = 4, 'Обожание'
        LOVE = 5, 'Любовь'

    grade = models.IntegerField(
        'оценка',
        choices=Grades.choices,
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        CustomUser,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        Item,
        verbose_name='товар',
        on_delete=models.CASCADE,
        related_name='some_item',
    )

    class Meta:
        unique_together = ('user', 'item')
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'

    def __str__(self):
        return self.get_grade()

    def get_grade(self):
        return self.Grades(self.grade).label
