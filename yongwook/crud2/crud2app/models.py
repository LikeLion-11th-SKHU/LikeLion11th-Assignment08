from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.CharField(max_length=20, default='me')
    url = models.URLField(max_length=200, default='www.naver.com')

    def __str__(self):
        return self.title