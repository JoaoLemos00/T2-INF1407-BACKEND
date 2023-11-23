from rest_framework import serializers
import sys
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from blog.models import BlogPost, CommentBlogPost

IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2 # 2MB
MIN_TITLE_LENGTH = 5
MIN_BODY_LENGTH = 50

class BlogPostSerializer(serializers.ModelSerializer):

	username = serializers.SerializerMethodField('get_username_from_author')

	class Meta:
		model = BlogPost
		fields = ['title','slug','body','image','date_updated','date_published','username']

	def get_username_from_author(self, blog_post):
		username = blog_post.author.username
		return username

    

class BlogPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'author']


    def create(self, validated_data):
        # Remova a chave 'image' do dicionário se não houver imagem presente
        image = validated_data.pop('image', None)

        # Crie a instância do BlogPost sem a imagem
        blog_post = BlogPost.objects.create(**validated_data)

        # Adicione a imagem se estiver presente
        if image:
            blog_post.image = image
            blog_post.save()

        return blog_post



class BlogPostUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image']


	
