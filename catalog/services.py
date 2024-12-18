from django.shortcuts import get_object_or_404
from django.core.cache import cache
from config.settings import CACHE_ENABLED

from catalog.models import Product, Category


def get_product_list_in_category(category):
    """Получение списка продуктов в определенной категории"""

    return Product.objects.filter(category=category)


def get_category(category):
    """Получение категории, чтобы передать в шаблон название категории"""

    return get_object_or_404(Category, id=category)


def get_categories():
    """Получение всех категорий"""

    return Category.objects.all()


def get_products_from_cache():
    """Получение продуктов из кэша, если кэш пуст, данные берутся из БД"""
    # если кэш не включен, мы возвращаем продукты сразу из базы данных
    if not CACHE_ENABLED:
        return Product.objects.all()

    # ключ для обращения к кэшу
    key = "products_list"
    # обращение к django для получения кэша по ключу
    products = cache.get(key)
    if products is not None:
        return products

    # если мы не получили продукты из кэша, то нам надо сначала получить продукты, а потом положить их в кэш
    products = Product.objects.all()
    cache.set(key, products, timeout=60 * 15)  # 15 минут
    return products


def get_categories_from_cache():
    """Получение категорий из кэша, если кэш пуст, данные берутся из БД"""
    # если кэш не включен, мы возвращаем категории сразу из базы данных
    if not CACHE_ENABLED:
        return Category.objects.all()

    # ключ для обращения к кэшу
    key = "categories_list"
    # обращение к django для получения кэша по ключу
    categories = cache.get(key)
    if categories is not None:
        return categories

    # если мы не получили категории из кэша, то нам надо сначала получить категории, а потом положить их в кэш
    categories = Category.objects.all()
    cache.set(key, categories, timeout=60 * 15)  # 15 минут
    return categories
