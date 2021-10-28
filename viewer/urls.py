from django.urls import path
from .views import hello, movies, genres, MovieView, MovieDetailView

urlpatterns = [
    path('hello/<s0>', hello),
    path('', movies, name='index'),
    path('genres/', genres, name='genres_lst'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/', MovieView.as_view(), name='movies')
]