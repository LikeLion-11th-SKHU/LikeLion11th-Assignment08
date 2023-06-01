from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100) 
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.CharField(max_length=20, default='me')
    mail = models.EmailField(max_length=30, default='kyw4846@gmail.com')

    def __str__(self):
        return self.title
    