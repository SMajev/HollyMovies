from django.contrib import admin
from .models import Genre, Movie, CommentMovie




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


@admin.register(CommentMovie)
class ComMovAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'movie', 'publish', 'edit',  
    )