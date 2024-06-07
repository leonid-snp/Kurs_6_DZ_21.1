from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Почта',
        help_text='Введите почту'
    )

    photo = models.ImageField(
        upload_to='users/',
        verbose_name='Аватар',
        help_text='Загрузите аватар',
        **NULLABLE
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='Телефон',
        help_text='Введите номер телефона',
        **NULLABLE
    )
    country = models.CharField(
        max_length=40,
        verbose_name='Страна',
        help_text='Введите название страны',
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
