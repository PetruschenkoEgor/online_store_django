from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.models import Contact, Product


class ProductTemplateView(TemplateView):
    """ Главная страница """
    template_name = "home.html"
    products = Product.objects.filter(id__lt=4)
    extra_context = {"products": products}


class ProductListView(ListView):
    """ Список продуктов с пагинацией """
    model = Product
    paginate_by = 3
    template_name = "catalog.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    """ Информация о продукте """
    model = Product
    template_name = "product.html"
    context_object_name = "product"


class ContactTemplateView(TemplateView):
    """ Контакты """
    template_name = "contacts.html"
    contact = Contact.objects.get(id=2)
    extra_context = {"contact": contact}


class ProductCreateView(CreateView):
    """ Добавление продукта """
    model = Product
    fields = ("name", "description", "image", "category", "price")
    template_name = "add_product.html"
    success_url = reverse_lazy("catalog:catalog")


class ProductUpdateView(UpdateView):
    """ Редактирование продукта """
    model = Product
    fields = ("name", "description", "image", "category", "price")
    template_name = "add_product.html"
    success_url = reverse_lazy("catalog:catalog")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    """ Удаление продукта """
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:catalog")
