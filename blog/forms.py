from django.forms import BooleanField, ModelForm

from blog.models import Article


class StyleFormMixin:
    """ Стилизация формы """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ArticleForm(StyleFormMixin, ModelForm):
    """ Форма со всеми полями статьи блога, которая будет отображаться в шаблонах """
    class Meta:
        """ Модель и поля формы """
        model = Article
        fields = '__all__'
