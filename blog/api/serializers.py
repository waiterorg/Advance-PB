from rest_framework import serializers
from blog.models import Article
from account.models import User

class ArticleSerializers(serializers.ModelSerializer):
    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }
    author = serializers.SerializerMethodField('get_author')
    
    class Meta:
        model = Article
        fields = "__all__"

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']