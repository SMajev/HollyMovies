from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    publish = models.DateTimeField(default=timezone.now())
    update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment add by {self.author} to post {self.post}'
    
    def save(self, *args, **kwargs): # new
        return super().save(*args, **kwargs)
    

