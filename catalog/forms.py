import os

from django import forms
from django.forms import BooleanField

from .models import Product


WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    """Форма с полями name, description, image, category, price, которая будет отображаться в шаблонах"""

    def __init__(self, *args, **kwargs):
        """Стилизация формы"""
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"

    class Meta:
        """Модель и поля формы"""

        model = Product
        fields = "__all__"

    def clean_price(self):
        """Валидатор цены(не отрицательная)"""
        price = self.cleaned_data.get("price")
        if price < 0:
            self.add_error("price", "Цена не может быть отрицательной!")
        return price

    def clean_image(self):
        """Валидатор изображения(только JPEG, PNG и не больше 5 МБ)"""
        image = self.cleaned_data.get("image")

        if image:
            # Проверяем формат изображения
            extension = ["jpg", "png"]
            file = os.path.splitext(image.name)[1].lower()[1:]
            if file not in extension:
                self.add_error(
                    "image", "Формат изображения может быть только JPG или PNG!"
                )

            # Проверяем, что размер изображения не превышает максимальный
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                self.add_error("image", f"Размер файла не должен превышать 5 МБ!")
        return image

    def clean(self):
        """Добавлен список слов-исключений для названия и описания"""
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in WORDS:
            if word in name.lower():
                self.add_error("name", f"Название не может содержать слово {word}!")
            if word in description.lower():
                self.add_error(
                    "description", f"Описание не может содержать слово {word}!"
                )
