from django.db import models
from django.utils import timezone


class BlogPostModel(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    author = models.CharField(default='Fancy Blogger', max_length=30)


class CommentModel(models.Model):
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField(max_length=350)
    name = models.CharField(default='Anonymous', max_length=30)
    post = models.ForeignKey('BlogPostModel', related_name='comments')

