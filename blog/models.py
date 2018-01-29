from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdown import markdown
from django.utils.html import strip_tags
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
    views = models.PositiveIntegerField(default=0)

    def save(self,*args,**kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个markdown类，用于渲染body的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdow.extensions.codehilite',

            ]
            )
            #先将markdown文本渲染成html文本
            #strip_tags去掉html文本的全部html标签
            #从文本摘取前54个字符赋给excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]
            #调用父类的save方法将数据保存到数据库中
            super(Post,self).save(*args,**kwargs)


    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']

