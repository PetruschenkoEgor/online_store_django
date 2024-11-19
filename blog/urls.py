from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", ArticleListView.as_view(), name="blog"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article"),
    path("article/new/", ArticleCreateView.as_view(), name="create"),
    path("article/<int:pk>/edit/", ArticleUpdateView.as_view(), name="update"),
    path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete"),
]
