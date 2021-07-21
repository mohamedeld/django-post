from django.db import models
import datetime

CATEGORY_CHOICES = (
    ('WB','web Developement'),
    ('DB','Desktop Developement'),
    ('DS','Data Science'),
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,unique=True)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(blank=True, default=datetime.datetime.now)
    published = models.BooleanField(default=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    view_count = models.IntegerField(default=0)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length=20)

    def __str__(self):
        return self.title
