# Generated by Django 5.1.2 on 2024-11-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название записи",
                        max_length=250,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Введите текст поста", verbose_name="Текст поста"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото для поста",
                        null=True,
                        upload_to="blog/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата создания"),
                ),
                (
                    "sign_of_publication",
                    models.BooleanField(verbose_name="Признак публикации"),
                ),
                (
                    "views_counter",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Введите количество просмотров",
                        verbose_name="Счетчик просмотров",
                    ),
                ),
            ],
        ),
    ]
