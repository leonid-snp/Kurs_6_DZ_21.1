# Generated by Django 5.0.6 on 2024-06-02 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_blog_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateField(
                default=datetime.date(2024, 6, 2),
                help_text="Укажите дату создания",
                verbose_name="Дата создания",
            ),
        ),
    ]
