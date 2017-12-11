from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class   Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)#标题
    body =  models.TextField()#正文
    created_time = models.DateTimeField()#创建时间
    modified_time = models.DateTimeField()#修改时间
    excerpt = models.CharField(max_length=200,blank=True)#摘要，可以为空
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']
