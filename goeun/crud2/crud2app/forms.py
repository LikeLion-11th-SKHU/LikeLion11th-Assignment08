from django import forms
from .models import Post

class PostForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ['title','body','user','age'] #입력받을 필드