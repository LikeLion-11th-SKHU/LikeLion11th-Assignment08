from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.CharField(max_length = 20, default=False)
    email = models.EmailField(default= "user.example.com")
    

    def __str__(self):
        return self.title