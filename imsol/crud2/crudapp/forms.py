from django import forms
from .models import Blog

class BlogFrom(forms.ModelForm):
    class Meta:
        model = Blog
        fields ={'title','body'}