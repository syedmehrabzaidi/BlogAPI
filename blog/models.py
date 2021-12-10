from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField

from blog_project.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    likes = models.ManyToManyField(AUTH_USER_MODEL, related_name='blogpost_like')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def number_of_likes(self):
        return self.likes.count()


class Comments(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             )
    comments = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comments


class ApiLogs(models.Model):
    url = models.CharField(default="", max_length=10000)
    method = models.CharField(default="", max_length=10)
    host = models.CharField(default="", max_length=100)
    query_parameters = JSONField(default=dict())
    username = models.CharField(default="", max_length=100)
    time = models.DateTimeField(auto_now_add=True)
