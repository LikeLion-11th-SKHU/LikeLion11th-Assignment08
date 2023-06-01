from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.POST['title']
    post.pub_date = timezone.now()
    post.body = request.POST['body']
    post.author = request.POST['author']
    post.email = request.POST['email']
    post.save()
    return redirect('read')

def read(request):
    posts = Post.objects
    return render(request, 'read.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'detail.html', {'post': post})

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'edit.html', {'edit_post': edit_post})

def update(request, id):
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.author = request.POST['author']
    update_post.email = request.POST['email']
    update_post.save()
    return redirect('read')

def delete(request, id):
    delete_post = get_object_or_404(Post, id = id)
    delete_post.delete()
    return redirect('read')