from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_page, add_product, catalog

# Создаем пространство имен, чтобы не хардкодить создаем через класс CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>/", product_page, name="product"),
    path("add/", add_product, name="add"),
    path("catalog/", catalog, name="catalog"),
]
