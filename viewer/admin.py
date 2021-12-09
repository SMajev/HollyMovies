from django.contrib import admin
from .models import Genre, Movie, CommentMovieModel


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['title', 'created']}),
        (
            'External Information',
            {
                'fields': ['genre', 'released'],
                'description': (
                    'These fields are going to be filled with data parsed'
                    'from external databases.'
                )
            }
        ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': 'These fields are intended to be fileed in our users'
            }
        )
    ]

    readonly_fields = ['created']

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id']
    list_display = [ 'id',
        'title','slug', 'genre',
        'rating', 'released_year'
    ]
    list_display_links = ['id', 'title']
    list_per_page = 20
    list_filter = ['genre', 'rating']  
    search_fields = ['title']
    actions = ['cleanup_description']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(CommentMovieModel)
class ComMovAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'movie', 'publish', 'update',  
    )

