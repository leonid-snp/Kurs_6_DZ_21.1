from django.db import models
from catalog.models import Product


NULLABLE = {"blank": True, "null": True}


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        help_text='Введите название продукта',
        related_name='Продукты',
    )
    number = models.IntegerField(
        verbose_name='Номер версии',
        help_text='Введите номер версии'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
        help_text='Введите название версии',
    )
    is_activ = models.BooleanField(
        verbose_name='Статус',
        help_text='Введите статус версии',
        default=True
    )

    def __str__(self):
        return f"{self.name} - {self.number}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
