from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit= False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = PostForm
        return render(request, 'create.html', {'form': form})

def read(request) :
    blogs = Post.objects.all()
    return render(request, 'read.html', {'blogs': blogs})

def detail(request,id) :
    blog = get_object_or_404(Post, id = id)
    return render(request, 'detail.html', {'blog':blog})


def update(request,id) :
    blog = get_object_or_404(Post, id =id) 
    if request.method == 'POST' :
        form = PostForm(request.POST, instance = blog)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date =timezone.now()
            form.save()
            return redirect('read')
        
    else:
        form = PostForm(instance = blog)
        return render(request, 'update.html',{'form':form})

def delete(request, id) :
    blog = get_object_or_404(Post, id =id) 
    blog.delete()
    return redirect('read')
