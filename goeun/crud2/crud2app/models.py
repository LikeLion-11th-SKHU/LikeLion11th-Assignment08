from django.db import models


# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.CharField(max_length=20, default='')
    age = models.PositiveIntegerField(help_text="User Age", blank=False, null=False)


    def __str__(self) :
        return self.title
