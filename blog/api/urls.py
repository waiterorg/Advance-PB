from django.urls import path
from .views import ArticleList

app_name = "api"
urlpatterns = [
    path('', ArticleList.as_view(), name='api_article_list'),
]