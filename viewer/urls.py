from django.urls import path
from django.conf.urls.static import static
from hollymovies import settings
from .views import (GenresList, MovieView, MovieDetailView, 
                        MovieCreateView, GenreCreateView,
                        MovieUpdateView, MovieDeleteView, GenreUpdateView,
                        GenreDeleteView, GenreDetailView
                    )


urlpatterns = [
    path('genres/', GenresList.as_view(), name='genres_lst'),   
    path('', MovieView.as_view(), name='movies'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('g/<int:pk>', GenreDetailView.as_view(), name='genre-detail'),
    path('new_movie/', MovieCreateView.as_view(), name='movie-create'),
    path('<int:pk>/medit', MovieUpdateView.as_view(), name='movie-update'),
    path('<int:pk>/mdelete', MovieDeleteView.as_view(), name='movie-delete'),
    path('new_genre/', GenreCreateView.as_view(), name='genre-create'),
    path('<int:pk>/gedit', GenreUpdateView.as_view(), name='genre-update'),
    path('<int:pk>/gdelete', GenreDeleteView.as_view(), name='genre-delete')
]

urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT
                    )