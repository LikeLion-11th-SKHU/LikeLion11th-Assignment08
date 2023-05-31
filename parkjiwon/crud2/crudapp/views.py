from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.utils import timezone
from .models import Blog

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = BlogForm()
        return render(request, 'create.html', {'form': form})

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'read.html', {'blogs': blogs})

def detail(request, title):
    blog = get_object_or_404(Blog, title=title)
    return render(request, 'detail.html', {'blog': blog, 'title': title})

