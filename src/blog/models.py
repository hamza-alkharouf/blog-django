import re
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
class Post(models.Model):
    #CharField jast one line
    title = models.CharField(max_length=100)
    #TextField many line
    content = models.TextField()

    post_date = models.DateTimeField(default=timezone.now)
    #auto_now each upate post 
    post_update = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return '/detail/{}'.format(self.pk)
        return reverse('detail', args=[self.pk])


    class Meta:
        ordering =('-post_date', )
 

class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name= 'البريد الاكتروني')
    body = models.TextField(verbose_name= 'التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return '.علق {} على {} '.format(self.name, self.post)

    class Meta:
        ordering =('-comment_date', )    