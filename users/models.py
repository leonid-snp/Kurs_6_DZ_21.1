from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog.models import NULLABLE


class Users(AbstractUser):
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

    )
