from rest_framework import routers
from django.urls import path, include
from .views import ArticleViewSet, UserViewSet

app_name = "api"

router = routers.SimpleRouter()
# router.register('users', UserViewSet)
router.register('articles', ArticleViewSet, basename='article')
router.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('',include(router.urls)),
]