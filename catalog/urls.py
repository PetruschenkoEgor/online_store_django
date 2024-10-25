from django.urls import path
from catalog.apps import CatalogConfig


# Создаем пространство имен, чтобы не хардкодить создаем через класс CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('')
]
