from django.contrib import admin
from .models import Genre, Movie, CommentMovieModel




@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'genre',
        'rating', 'released'
    )
    list_filter = ('genre', 'rating')
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(CommentMovieModel)
class ComMovAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'movie', 'publish', 'update',  
    )