from django.db import models

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=100,default='')
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.CharField(max_length=100,default='') #작성자 생성
    email = models.EmailField(max_length=132,default='') #필드 추가

    
  

    def __str__(self) :
        return self.title