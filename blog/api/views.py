from blog.models import Article
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import ArticleSerializers
# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
