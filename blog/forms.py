from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        labels = {'title': 'Título',
        		  'text': 'Publicación'}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        labels = {'author': 'Autor',
        		  'text': 'Comentario'}