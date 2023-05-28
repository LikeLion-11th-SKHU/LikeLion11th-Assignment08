from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    username = models.CharField(max_length=20, verbose_name="사용자명", default='guest')
    useremail = models.EmailField(max_length=254, verbose_name = "사용자 이메일", default='example@example.com')
    userword = models.CharField(max_length=64, verbose_name="비밀번호", default='default_password')
    
    def __str__(self):
        return self.title