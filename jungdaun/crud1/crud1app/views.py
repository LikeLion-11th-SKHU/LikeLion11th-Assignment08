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
    blog.body = request.POST['username']
    boolean_value = request.POST.get('boolean', False) == 'True'
    blog.body = boolean_value
    blog.save()
    return redirect('read')

def read(request):
    blogs = Blog.objects
    return render(request, 'read.html', {'blogs' : blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    return render(request, 'detail.html', {'blog' : blog})

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'edit_blog' : edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.body = request.POST['username']
    boolean_value = request.POST.get('boolean', False) == 'True'
    update_blog.body = boolean_value
    update_blog.save()
    return redirect('read') 

def delete(request, id):
    delete_blog = get_object_or_404(Blog, id = id)
    delete_blog.delete()
    return redirect('read') 