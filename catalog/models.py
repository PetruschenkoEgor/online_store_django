from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание товара', blank=True, null=True)
    image = models.ImageField(upload_to='catalog/photo', verbose_name='Фото', help_text='Загрузите фото продукта', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='Категория', help_text='Введите категорию', blank=True, null=True, related_name='products')
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену продукта')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price']

    def __str__(self):
        return f'{self.name} - {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание категории', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
