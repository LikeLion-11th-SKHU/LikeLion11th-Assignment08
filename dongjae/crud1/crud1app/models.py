from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    author = models.CharField(max_length=20, default="unknown")
    comment_allow = models.BooleanField(default=False) # 추가 필드

    def __str__(self):
        return self.title