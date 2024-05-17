# Generated by Django 5.0.6 on 2024-05-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_content_blog_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="created_at",
            field=models.DateField(
                blank=True,
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="is_published",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="Укажите статус публикации",
                null=True,
                verbose_name="Публикация",
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото",
                null=True,
                upload_to="blogs/",
                verbose_name="Фото",
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="slug",
            field=models.CharField(
                blank=True,
                help_text="Введите slug",
                max_length=60,
                null=True,
                verbose_name="slug",
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="views_count",
            field=models.IntegerField(
                blank=True,
                default=0,
                help_text="Количество просмотров",
                null=True,
                verbose_name="Просмотры",
            ),
        ),
    ]