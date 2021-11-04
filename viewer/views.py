from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator
from .models import Movie, Genre


class GenresList(ListView):
    template_name = 'genres.html'
    model = Genre
    context_object_name = 'genres'


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie
    context_object_name = 'movie'


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'
    paginate_by = 20

    def get_queryset(self):
        sorting = self.request.GET.get('s') or ''
        if sorting:
            context = super().get_queryset().order_by(sorting)
        else:
            context = super().get_queryset().all()
        return context


class GenreMoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = self.request.GET.get('genre')
        context['movies'] = context['movies'].filter(genre__name=genre)
        return context
        




