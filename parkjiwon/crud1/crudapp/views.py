from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.pub_date = timezone.now()
    blog.body = request.POST['body']
    blog.writer = request.POST['writer']
    blog.age = int(request.POST['age'])
    blog.save()
    return redirect('read')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'read.html', {'blogs': blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    return render(request, 'detail.html', {'blog': blog})
