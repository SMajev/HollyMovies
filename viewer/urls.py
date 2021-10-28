from django.urls import path

from .views import hello, movies, genres

urlpatterns = [
    path('hello/<s0>', hello),
    path('movies/', movies, name='index'),
    path('genres/', genres, name='genres_lst')
]