from django.db import models


NULLABLE = {"blank": True, "null": True}


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
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        **NULLABLE
    )
    updated_at = models.DateField(
        verbose_name="Дата изменения",
        help_text="Укажите дату изменения",
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
