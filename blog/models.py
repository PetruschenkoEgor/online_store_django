from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок',
        help_text='Введите название записи',
    )
    content = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст поста',
    )
    image = models.ImageField(
        upload_to='blog/photo',
        verbose_name='Фото',
        help_text='Загрузите фото для поста',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    sign_of_publication = models.BooleanField(verbose_name='Признак публикации')
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Введите количество просмотров',
        default=0,
    )
