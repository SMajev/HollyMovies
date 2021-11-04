from django.urls import path
from .views import GenresList, MovieView, MovieDetailView, GenreMoviesView



urlpatterns = [
    path('', MovieView.as_view(), name='index'),
    path('genres/', GenresList.as_view(), name='genres_lst'),   
    path('', MovieView.as_view(), name='movies'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('genre/', GenreMoviesView.as_view(), name='filtered-movies')
]