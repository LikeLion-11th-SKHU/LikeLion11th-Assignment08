from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data pubished')
    body = models.TextField()
    name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.title
    
    