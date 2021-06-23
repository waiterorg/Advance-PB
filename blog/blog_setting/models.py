from django.db import models

# Create your models here.

class SettingsManager(models.Manager):
    def get_active(self):
        active = Settings.objects.get(active=True)
        return active



class Settings(models.Model):
    
    name = models.CharField(max_length=100,verbose_name='نام سایت')
    logo = models.ImageField(upload_to = 'site_image',verbose_name='لوگو سایت')
    copyright = models.CharField(max_length=120,verbose_name='قانون کپی رایت / صاحب سایت')
    description = models.CharField(max_length=150,verbose_name='معرفی سایت')
    active = models.BooleanField(verbose_name='فعال / غیر فعال', default=False)
    objects = SettingsManager()
    
    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'
    
    def __str__(self):
        return self.name
