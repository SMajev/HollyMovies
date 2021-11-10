from django.db import models
from django.contrib.auth.models import User

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
    image = models.FileField(upload_to='./media/movies/covers', default='download.jpg')

    def __str__(self):
        return self.title

class CommentMovie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    publish = models.DateTimeField()
    edit = models.DateTimeField()
    body = models.TextField()
