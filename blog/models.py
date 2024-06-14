from django.db import models
from config.settings import NULLABLE


class Blog(models.Model):
    title = models.CharField(
        max_length=60,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
        default=None
    )
    slug = models.CharField(
        max_length=60,
        verbose_name="slug",
        help_text="Введите slug",
        **NULLABLE
    )
    content = models.TextField(
        verbose_name="Текст",
        help_text="Введите текст",
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to="blogs/",
        verbose_name="Фото",
        help_text="Загрузите фото",
        **NULLABLE
    )
    created_at = models.DateField(
        auto_now_add=True,
        **NULLABLE
    )
    is_published = models.BooleanField(
        verbose_name="Публикация",
        help_text="Укажите статус публикации",
        default=True,
        **NULLABLE
    )
    views_count = models.IntegerField(
        verbose_name="Просмотры",
        help_text="Количество просмотров",
        default=0,
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        permissions = [
            ('change_content_blog', 'Change content blog'),
            ('change_title_blog', 'Change title blog'),
            ('unpublish_a_blog', 'Unpublish a blog')
        ]
