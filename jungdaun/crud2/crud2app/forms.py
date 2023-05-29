from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'username', 'useremail', 'userword']