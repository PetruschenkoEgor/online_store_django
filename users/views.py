from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    """Регистрация пользователя"""

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject="Вы успешно зарегистрировались",
            message="Приветствуем Вас в нашем интернет магазине! Вы успешно зарегистрировались и может войти в свой личный кабинет!",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    """Редактирование пользователя"""

    model = User
    form_class = UserRegisterForm
    template_name = "users/user_form.html"
    success_url = "users:login"

    def get_success_url(self):
        """Перенаправление"""
        return reverse_lazy("users:login")
