from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts


# Создаем пространство имен, чтобы не хардкодить создаем через класс CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
