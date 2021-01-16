from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.author.username})'

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blog:post_list')