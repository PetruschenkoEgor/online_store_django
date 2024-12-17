from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ContactTemplateView,
    ProductTemplateView, ProductCategoryListView,
)

# Создаем пространство имен, чтобы не хардкодить создаем через класс CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path("home/", ProductTemplateView.as_view(), name="home"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", cache_page(60 * 15)(ProductDetailView.as_view()), name="product"),
    path("add/", ProductCreateView.as_view(), name="add"),
    path("catalog/", ProductListView.as_view(), name="catalog"),
    path("category/<int:category_id>/", ProductCategoryListView.as_view(), name="category"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),
]
