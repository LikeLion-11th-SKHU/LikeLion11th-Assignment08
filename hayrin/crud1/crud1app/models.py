from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title