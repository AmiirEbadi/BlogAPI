from urllib import request
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError
)
from django.contrib.auth import get_user_model
from article.models import Article


class UserSerializer(ModelSerializer):
    # for serializing user fields

    class Meta:
        model = get_user_model()
        fields = ['first_name' , 'last_name' , 'username' , 'Position']

class AuthorFieldSerializer(ModelSerializer):
    #used for serializing PostSerializer ForignKey 

    class Meta:
        model = get_user_model()
        fields = ['username']

class PostSerializer(ModelSerializer):
    author = AuthorFieldSerializer(read_only = True)
    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def validate(self, data):
        if len(data['body']) < 30:
            raise ValidationError('The body of this article is too short , it must be more than 20 Char')
        return data
    