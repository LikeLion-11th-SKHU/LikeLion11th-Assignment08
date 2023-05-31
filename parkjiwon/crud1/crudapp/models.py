from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    writer = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.title
    

