from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.core.paginator import Paginator
from .models import Movie, Genre, CommentMovie
from django.views.generic.edit import FormMixin
from .forms import MovieForm
from .models import Movie, Genre
from django.urls import reverse_lazy
from logging import getLogger

LOGGER = getLogger()

class MovieCreateView(FormView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title = cleaned_data['title'],
            genre = cleaned_data['genre'],
            rating = cleaned_data['rating'],
            released = cleaned_data['released'],
            description = cleaned_data['description']
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provides wrong data.')
        return super().form_invalid(form)

class GenresList(ListView):
    template_name = 'genres.html'
    model = Genre
    context_object_name = 'genres'


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie
    context_object_name = 'movie'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pk'] = self.object.pk
        context['movie'] = get_object_or_404(Movie,
                                                pk=self.kwargs['pk']
                                            )
        context['comments'] = CommentMovie.objects.all()
        return context



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
        




