from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    rating = models.FloatField()
    released = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='covers', default='download.jpg')

    def __str__(self):
        return self.title

class CommentMovieModel(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment add by {self.author} to post {self.movie}'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
