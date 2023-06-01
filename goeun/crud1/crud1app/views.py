from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def new(request) :
    return render(request, 'new.html')

# new를 통해 전달받은 데이터를 추가하고 저장해주는 함수 작성
def create(request) :
    blog = Post()
    blog.title = request.POST['title']
    blog.pub_date = timezone.now()
    blog.body = request.POST['body']
    blog.user = request.POST['user']
    blog.email = request.POST['email']
    blog.save()
    return redirect('read')

def read(request) :
    blogs = Post.objects
    return render(request, 'read.html',{'blogs': blogs})

def detail(request, id) :
    blog = get_object_or_404(Post, id=id)
    return render(request, 'detail.html',{'blog':blog})