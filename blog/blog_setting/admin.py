from django.contrib import admin
from .models import Settings
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('name','active')


admin.site.register(Settings, SettingAdmin)