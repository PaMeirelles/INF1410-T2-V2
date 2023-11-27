# forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'autor', 'corpo', 'dt_publicado', 'status']
