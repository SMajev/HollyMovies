from django.urls import path
from .views import GenresList, MovieView, MovieDetailView, GenreMoviesView

urlpatterns = [
    path('', MovieView.as_view(), name='index'),
    path('genres/', GenresList.as_view(), name='genres_lst'),   
    path('movies/', MovieView.as_view(), name='movies'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('movies-genre/', GenreMoviesView.as_view(), name='filtered-movies')
]