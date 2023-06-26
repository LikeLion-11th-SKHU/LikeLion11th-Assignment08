from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post

# Create your views here.

def index02(request):
    return render(request, 'index02.html')

def create(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read02')
    else:
        form = PostForm
        return render(request, 'create.html',{'form':form})

def read02(request) :
    blogs = Post.objects.all()
    return render(request, 'read02.html', {'blogs': blogs})

def detail02(request,title) :
    blog = get_object_or_404(Post, title = title)
    return render(request, 'detail02.html', {'blog':blog})


def update02(request,title) :
    blog = get_object_or_404(Post, title =title) 
    if request.method == 'POST' :
        form = PostForm(request.POST, instance = blog)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date =timezone.now()
            form.save()
            return redirect('read02')       
    else:
        form = PostForm(instance = blog)
        return render(request, 'update02.html',{'form':form})

def delete02(request, title) :
    blog = get_object_or_404(Post, title =title) 
    blog.delete()
    return redirect('read02')
