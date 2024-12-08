from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Contact, Product


class ProductTemplateView(TemplateView):
    """Главная страница"""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """Передача объекта Product в шаблон"""

        context = super().get_context_data()
        context["products"] = Product.objects.filter(id__lt=4)
        return context


class ProductListView(ListView):
    """Список продуктов с пагинацией"""

    model = Product
    paginate_by = 3
    template_name = "catalog.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Информация о продукте"""

    model = Product
    template_name = "product.html"
    context_object_name = "product"


class ContactTemplateView(TemplateView):
    """Контакты"""

    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        """Передача объекта Contact в шаблон"""

        context = super().get_context_data()
        context["contact"] = Contact.objects.get(id=2)
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Добавление продукта"""

    model = Product
    form_class = ProductForm
    template_name = "add_product.html"
    success_url = reverse_lazy("catalog:catalog")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование продукта"""

    model = Product
    form_class = ProductForm
    template_name = "add_product.html"
    success_url = reverse_lazy("catalog:catalog")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта"""

    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:catalog")
