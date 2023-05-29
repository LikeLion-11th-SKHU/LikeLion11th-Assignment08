from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    username = models.CharField(max_length=20, verbose_name="사용자명", default='guest')
    boolean = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title