from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_page

# Создаем пространство имен, чтобы не хардкодить создаем через класс CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>/", product_page, name="product"),
]
