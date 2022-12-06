from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        'имя',
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        'фамилия',
        max_length=150,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        'почта',
        unique=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    birthday = models.DateField(
        'день рождения',
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
