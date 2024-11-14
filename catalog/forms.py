from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """ Форма с полями name, description, image, category, price, которая будет отображаться в шаблонах """
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')
