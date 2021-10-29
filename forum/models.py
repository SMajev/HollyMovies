from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



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

    def __str__(self):
        return self.title
    

