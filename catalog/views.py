from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Contact, Product


class ProductTemplateView(TemplateView):
    """Главная страница"""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """Передача объекта Product в шаблон"""

        context = super().get_context_data()
        context["products"] = Product.objects.filter(id__lt=4)
        # права пользователя
        context["perms"] = {
            "products": {
                "can_unpublish_product": self.request.user.has_perm(
                    "catalog.can_unpublish_product"
                ),
                "can_delete_product": self.request.user.has_perm(
                    "catalog.delete_product"
                ),
                "can_change_product": self.request.user.has_perm(
                    "catalog.change_product"
                ),
            }
        }
        return context


class ProductListView(ListView):
    """Список продуктов с пагинацией"""

    model = Product
    paginate_by = 3
    template_name = "catalog.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        """Передача объекта Product в шаблон"""
        context = super().get_context_data(**kwargs)
        # права пользователя
        context["perms"] = {
            "products": {
                "can_unpublish_product": self.request.user.has_perm(
                    "catalog.can_unpublish_product"
                ),
                "can_delete_product": self.request.user.has_perm(
                    "catalog.delete_product"
                ),
                "can_change_product": self.request.user.has_perm(
                    "catalog.change_product"
                ),
            }
        }
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Информация о продукте"""

    model = Product
    template_name = "product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        """Передача объекта Product в шаблон"""
        context = super().get_context_data(**kwargs)
        # права пользователя
        context["perms"] = {
            "products": {
                "can_unpublish_product": self.request.user.has_perm(
                    "catalog.can_unpublish_product"
                ),
                "can_delete_product": self.request.user.has_perm(
                    "catalog.delete_product"
                ),
                "can_change_product": self.request.user.has_perm(
                    "catalog.change_product"
                ),
            }
        }
        return context


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

    def form_valid(self, form):
        """При создании продукта, ему сразу же присваивается текущий пользователь как собственник"""
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование продукта"""

    model = Product
    form_class = ProductForm
    template_name = "add_product.html"
    success_url = reverse_lazy("catalog:catalog")

    def get_success_url(self):
        """Перенаправление"""
        return reverse("catalog:product", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        """Редактировать могут Модераторы продуктов или собственники"""
        user = self.request.user
        # если у пользователя есть определенные права на редактирование признака публикации
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        # или пользователь владелец продукта
        elif user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта"""

    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:catalog")

    def dispatch(self, request, *args, **kwargs):
        """Удалять могут Модераторы продуктов или собственники"""
        user = self.request.user
        product = self.get_object()
        # если у пользователя есть определенные права на удаление продукта
        # или пользователь владелец продукта
        if user.has_perm("catalog.delete_product") or user == product.owner:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
