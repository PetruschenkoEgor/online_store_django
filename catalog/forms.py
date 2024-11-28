from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """Форма с полями name, description, image, category, price, которая будет отображаться в шаблонах"""

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in name.lower():
                self.add_error('name', f'Название не может содержать слово {word}!')
            elif word in description.lower():
                self.add_error('description', f'Описание не может содержать слово {word}!')
