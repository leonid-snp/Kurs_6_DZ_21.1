# Generated by Django 4.2 on 2024-06-14 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "name", "price", "created_at", "updated_at"],
                "permissions": [
                    ("unpublish_a_product", "Unpublish a product"),
                    ("change_product_description,", "Change description"),
                    ("change_product_category", "Change product category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
