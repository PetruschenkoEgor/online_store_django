from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article


class ArticleListView(ListView):
    """ Список постов блога """
    model = Article
    paginate_by = 10
    template_name = 'blog.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    """ Детали статьи """
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        """ Увеличение количества просмотров """
        self.object = super().get_object()
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    """ Добавление поста """
    model = Article
    fields = ('title', 'content', 'image', 'sign_of_publication')
    template_name = 'article_form.html'
    success_url = reverse_lazy('blog:blog')


class ArticleUpdateView(UpdateView):
    """ Редактирование статьи """
    model = Article
    fields = ('title', 'content', 'image', 'sign_of_publication')
    template_name = 'article_form.html'
    success_url = reverse_lazy('blog:blog')

    def get_success_url(self):
        """ Перенаправление на статью """
        return reverse('blog:article', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    """ Удаление статьи """
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('blog:blog')
