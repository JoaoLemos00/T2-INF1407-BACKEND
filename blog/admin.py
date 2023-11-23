from django.contrib import admin

from blog.models import BlogPost,CommentBlogPost

admin.site.register(BlogPost)
admin.site.register(CommentBlogPost)

# Register your models here.
