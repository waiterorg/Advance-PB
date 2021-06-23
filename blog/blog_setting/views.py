from django.shortcuts import render
from .models import Settings
# Create your views here.

def header(request):
    settings = Settings.objects.get_active()

    context = {
        'settings': settings ,
    }
    return render(request, 'shared/header_for_home.html', context)