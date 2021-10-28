from django.urls import path
from .views import hello, movies, genres, MovieView

urlpatterns = [
    path('hello/<s0>', hello),
    path('', movies, name='index'),
    path('genres/', genres, name='genres_lst'),
    path('movies/', MovieView.as_view(), name='movies')
]