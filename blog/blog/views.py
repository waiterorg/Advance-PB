from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from account.models import User
from django.db.models import Count, Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from account.mixins import AuthorAccessMixin
from datetime import datetime, timedelta
from django.db.models import Q
# Create your views here.


class ArticleListView(ListView):
    last_month = datetime.today() - timedelta(days=30)
    queryset = Article.objects.get_published_article()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_month = datetime.today() - timedelta(days=30)
        context['popular_articles'] = Article.objects.get_published_article().annotate(count=Count('hits', filter=Q(articlehit__created__gte=last_month))).order_by('-count', '-publish')[:5]
        return context



#Q(articlehit__year=2020)
#Q(articlehit__month=12)


class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = Article.objects.get_published_article()
        article = get_object_or_404(article, slug=slug)

        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

        return article


class ArticlePreview(AuthorAccessMixin, DetailView):

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)


class CategoryList(ListView):
    paginate_by = 2
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(
            Category.objects.get_active_category(), slug=slug)
        return category.articles.get_published_article()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    paginate_by = 2
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.article.get_published_article()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context


class SearchList(ListView):
    paginate_by = 2
    template_name = 'blog/search_list.html'

    def get_queryset(self):
        global author
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
