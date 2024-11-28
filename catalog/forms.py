from django import forms
from django.forms import BooleanField

from .models import Product


class ProductForm(forms.ModelForm):
    """Форма с полями name, description, image, category, price, которая будет отображаться в шаблонах"""

    def __init__(self, *args, **kwargs):
        """ Стилизация формы """
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'

    class Meta:
        """ Модель и поля формы """
        model = Product
        fields = '__all__'

    def clean_price(self):
        """ Валидатор цены """
        price = self.cleaned_data.get('price')
        if price < 0:
            self.add_error('price', 'Цена не может быть отрицательной!')

    def clean(self):
        """ Добавлен список слов-исключений для названия и описания """
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in name.lower():
                self.add_error('name', f'Название не может содержать слово {word}!')
            elif word in description.lower():
                self.add_error('description', f'Описание не может содержать слово {word}!')
