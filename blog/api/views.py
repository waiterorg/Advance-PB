from blog.models import Article
from account.models import User
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ArticleSerializers, UserSerializers
# Create your views here.


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers