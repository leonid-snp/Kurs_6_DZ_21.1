from django.db import models
from users.models import User
from config.settings import NULLABLE


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to="products/",
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите название категории",
        related_name="Products",
        **NULLABLE
    )
    price = models.IntegerField(
        verbose_name="Цена продукта",
        help_text="Введите цену продукта",
        **NULLABLE
    )
    created_at = models.DateField(
        auto_now_add=True,
        **NULLABLE
    )
    updated_at = models.DateField(
        auto_now=True,
        **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        help_text='Укажите владельца',
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    is_published = models.BooleanField(
        verbose_name="Публикация",
        help_text="Укажите статус публикации",
        default=True,
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "category", "name", "price",
            "created_at", "updated_at"
        ]
        permissions = [
            ('unpublish_a_product', 'Unpublish a product'),
            ('change_description,', 'Change description'),
            ('change_category', 'Change category')
        ]


class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название контакта",
        help_text="Введите название контакта",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Номер контакта",
        help_text="Введите номер контакта",
    )
    message = models.TextField(
        verbose_name="Сообщение",
        help_text="Введите сообщение",
        **NULLABLE
    )

    def __str__(self):
        return f"{self.name} {self.phone}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = [
            "name", "phone"
        ]
