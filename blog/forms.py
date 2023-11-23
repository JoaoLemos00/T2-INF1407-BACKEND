from django import forms

from blog.models import BlogPost, CommentBlogPost

class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']

class UpdateBlogPostFrom(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']

        def save(self,commit = True):
            blog_post = self.instance
            blog_post.title = self.cleaned_data['title']
            blog_post.body = self.cleaned_data['body']
            
            if self.cleaned_fata['image']:
                blog_post.image = self.cleaned_data['image']

            if commit:
                blog_post.save()
                
            return blog_post

class CommentBlogPostForm(forms.ModelForm):

    class Meta:
        model = CommentBlogPost
        fields = ['body']


class UpdateCommentBlogPostForm(forms.ModelForm):

    class Meta:
        model = CommentBlogPost
        fields = ['body']

        def save(self,commit = True):
            blog_post_comment = self.instance
            blog_post_comment.body = self.cleaned_data['body']

            if commit:
                blog_post_comment.save()
                
            return blog_post_comment
