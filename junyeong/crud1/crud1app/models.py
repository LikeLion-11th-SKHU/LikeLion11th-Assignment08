from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    body = models.TextField()
    user_name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, default="")

    def __str__(self):
        return self.title
