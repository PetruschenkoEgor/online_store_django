from django.shortcuts import get_object_or_404

from catalog.models import Product, Category


def get_product_list_in_category(category):
    """ Получение списка продуктов в определенной категории """

    return Product.objects.filter(category=category)


def get_category(category):
    """ Получение категории, чтобы передать в шаблон название категории """

    return get_object_or_404(Category, id=category)


def get_categories():
    """ Получение всех категорий """

    return Category.objects.all()
