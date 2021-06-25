from blog.models import Article
from account.models import User
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ArticleSerializers, UserSerializers
from .permissions import IsSuperUserOrStaffReadOnly, IsStaffOrReadOnly, IsAuthorOrReadOnly
# Create your views here.


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    filterset_fields = ['status', 'author__username']
    search_fields = ['title', 'author__username',
                     'description', 'author__first_name', 'author__last_name']
    ordering_fields = ['status', 'is_special']
    ordering = ['-publish']

def get_permissions(self):
    """
    Instantiates and returns the list of permissions that this view requires.
    """
    if self.action in ['list', 'create']:
        permission_classes = [IsStaffOrReadOnly]
    else:
        permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
    return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filterset_fields = ['is_staff']
    search_fields = ['username']
    ordering_fields = ['special_user']
    permission_classes = (IsSuperUserOrStaffReadOnly,)
