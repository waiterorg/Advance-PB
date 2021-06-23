from django.urls import path
from .views import header

app_name = "settings"
urlpatterns = [
    path('header', header, name="header"),   

]