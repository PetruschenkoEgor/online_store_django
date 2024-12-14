from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.mail import send_mail

from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(ListView):
    """Список постов блога"""

    model = Article
    paginate_by = 10
    template_name = "blog.html"
    context_object_name = "articles"

    def get_queryset(self):
        """Выводит только статьи с положительным признаком публикации"""
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_publication=True)
        return queryset

    def get_context_data(self, **kwargs):
        """Передача в шаблон"""
        context = super().get_context_data(**kwargs)
        context["perms"] = {
            "articles": {
                "change_article": self.request.user.has_perm("blog.change_article"),
                "delete_article": self.request.user.has_perm("blog.delete_article"),
            }
        }
        return context


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """Детали статьи"""

    model = Article
    template_name = "article.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        """Увеличение количества просмотров и отправка сообщения на почту яндекс каждые 100 просмотров"""
        self.object = super().get_object()
        self.object.views_counter += 1
        self.object.save()
        # Как только статья набирает каждые 100 просмотров, отправляется сообщение на почту яндекс
        if (self.object.views_counter % 100) == 0:
            send_mail(
                "Blog",
                f"Поздравляю, количество просмотров твоей статьи(id: {self.object.id}, название: "
                f"{self.object.title}) увеличилось на 100! Теперь {self.object.views_counter} просмотров!",
                settings.EMAIL_HOST_USER,
                ["petrushenko.jegor@ya.ru"],
            )
        return self.object

    def get_context_data(self, **kwargs):
        """Передача в шаблон"""
        context = super().get_context_data(**kwargs)
        context["perms"] = {
            "articles": {
                "change_article": self.request.user.has_perm("blog.change_article"),
                "delete_article": self.request.user.has_perm("blog.delete_article"),
            }
        }
        return context


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Добавление поста"""

    model = Article
    form_class = ArticleForm
    # fields = ("title", "content", "image", "sign_of_publication")
    template_name = "article_form.html"
    success_url = reverse_lazy("blog:blog")
    # обязательное право для добавления поста
    permission_required = "blog.add_article"


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование статьи"""

    model = Article
    form_class = ArticleForm
    # fields = ("title", "content", "image", "sign_of_publication")
    template_name = "article_form.html"
    success_url = reverse_lazy("blog:blog")
    # обязательное право для редактирования поста
    permission_required = "blog.change_article"

    def get_success_url(self):
        """Перенаправление на статью"""
        return reverse("blog:article", args=[self.kwargs.get("pk")])


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление статьи"""

    model = Article
    template_name = "article_confirm_delete.html"
    success_url = reverse_lazy("blog:blog")
    # обязательное право для удаления поста
    permission_required = "blog.delete_article"
