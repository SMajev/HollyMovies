from django.contrib import admin
from .models import Genre, Movie




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