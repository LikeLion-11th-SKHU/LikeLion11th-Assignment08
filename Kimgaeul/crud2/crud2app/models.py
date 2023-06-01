from django.db import models

# Create your models here.

class Blog(models.Model) :
    title = models.CharField(max_length=100, primary_key=True)
    pub_date = models.DateTimeField('data published')
    body = models.TextField() 
    gaeul = models.CharField(max_length=20)
    url = models.URLField(null=True, blank=True, default=None)
    # 필드 추가

    def __str__(self) :
        return self.title