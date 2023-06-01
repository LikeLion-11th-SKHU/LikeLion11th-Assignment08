from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    name = models.CharField(max_length=20)
    score = models.IntegerField(null=True)
    
    def __int__(self):
        return self.title
    
    
