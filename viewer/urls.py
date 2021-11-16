from django.urls import path
from django.conf.urls.static import static
from hollymovies import settings
from .views import (GenresList, MovieView, MovieDetailView, 
                        GenreMoviesView, MovieCreateView, GenreCreateView
                    )


urlpatterns = [
    path('', MovieView.as_view(), name='index'),
    path('genres/', GenresList.as_view(), name='genres_lst'),   
    path('', MovieView.as_view(), name='movies'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('genre/', GenreMoviesView.as_view(), name='filtered-movies'),
    path('new_movie/', MovieCreateView.as_view(), name='movie-create'),
    path('new_genre/', GenreCreateView.as_view(), name='genre-create')
]

urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT
                    )