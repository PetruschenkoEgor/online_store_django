from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, UserUpdateView

app_name = UsersConfig.name
urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="users:login"), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("user/<int:pk>/edit_user/", UserUpdateView.as_view(), name="user_update"),
]
