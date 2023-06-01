from django.db import models

# Create your models here.

class Blog(models.Model) :
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField() 
    gaeul = models.CharField(max_length=20) 
    # 작성자 추가
    id = models.AutoField(primary_key=True)
    # 필드 추가

    def __str__(self) :
        return self.title
