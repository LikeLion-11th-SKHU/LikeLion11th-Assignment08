from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request,'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    post=Post()
    post.title=request.POST['title']
    post.create_time=timezone.now()
    post.content=request.POST['content']
    post.name=request.POST['name']
    post.save()
    return redirect('read')

def read(request):
    posts=Post.objects
    return render(request, 'read.html', {'posts':posts})

def detail(request,title):
    post=get_object_or_404(Post, title=title)
    return render(request, 'detail.html', {'post':post})

def edit(request, title):
    edit_posts = Post.objects.get(title=title)
    return render(request, 'edit.html', {'edit_posts' : edit_posts})

def update(request, title):
    update_post = Post.objects.get(title=title)
    update_post.title = request.POST['title']
    update_post.create_time=timezone.now()
    update_post.content=request.POST['content']
    update_post.name=request.POST['name']
    update_post.save()
    return redirect('read')

def delete(request, tilte):
    delete_post = get_object_or_404(Post, tilte=tilte)
    delete_post.delete()
    return redirect('read')