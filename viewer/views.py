from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from logging import getLogger
from django.views.generic.edit import FormMixin
from .models import Movie, Genre, CommentMovieModel
from .forms import MovieForm, GenreForm, CommentMovie
from shapeshifter.views import MultiFormView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

LOGGER = getLogger()


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class SudoRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class GenreCreateView(StaffRequiredMixin, PermissionRequiredMixin, FormView):
    template_name = 'genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres_lst')
    permission_required = 'viewer.add_genre'
    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(
            name = cleaned_data['name']
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provides wrong data.')
        return super().form_invalid(form)


class GenreUpdateView(StaffRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'genre_form.html'
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('genres_lst')
    permission_required = 'viewer.change_genre'


class GenreDeleteView(StaffRequiredMixin, PermissionRequiredMixin,  DeleteView):
    template_name = 'movie_delete.html'
    model = Genre
    success_url = reverse_lazy('genres_lst')
    permission_required = 'viewer.delete_genre'


class MovieUpdateView(StaffRequiredMixin, PermissionRequiredMixin,  UpdateView):
    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.change_movie'


class MovieDeleteView(StaffRequiredMixin, PermissionRequiredMixin,  DeleteView):
    template_name = 'movie_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'


class MovieCreateView(StaffRequiredMixin, PermissionRequiredMixin,  FormView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        if not cleaned_data['genre']:
            cleaned_data['genre'] = Genre.objects.create(name=self.request.POST['newgen'])

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


class MovieDetailView(FormMixin, DetailView):
    model = Movie
    form_class = CommentMovie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = get_object_or_404(Movie, pk=self.kwargs['pk'])
        context['form'] = self.get_form()
        context['pk'] = self.object.pk
        context['comments'] = CommentMovieModel.objects.filter(
            movie=self.get_object()).order_by('-publish')   
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('movie-detail', kwargs={'pk': self.kwargs['pk'] })

    def post(self, request,*args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.movie = self.get_object()
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    
class MovieView(ListView, PermissionRequiredMixin):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'
    paginate_by = 10
    permission_required = 'viewer/view_movie'

    def get_queryset(self):
        sorting = self.request.GET.get('s') or ''
        if sorting:
            context = super().get_queryset().order_by(sorting)
        else:
            context = super().get_queryset().all()
        return context


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre_detail.html'
    context_object_name = 'genre'

    def get_success_url(self, **kwargs):
        return reverse_lazy('movie-detail', kwargs={'pk': self.kwargs['pk'] })
    
    def get_context_data(self, **kwargs):
        sorting = self.request.GET.get('s') or ''
        context = super().get_context_data(**kwargs)
        if sorting:
            context['movies'] = Movie.objects.filter(genre=self.get_object()).order_by(sorting)
        else:
            context['movies'] = Movie.objects.filter(genre=self.get_object())
        return context



# class GenreMoviesView(ListView):
#     template_name = 'movies.html'
#     model = Movie
#     context_object_name = 'movies'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         genre = self.request.GET.get('genre')
#         context['movies'] = get_object_or_404(Movie, genre=self.kwargs['pk'])
#         return context
        


# class GenreCreateView(CreateView):
#     model = Genre
#     fields = '__all__'
#     template_name = 'genre_form.html'
#     success_url = reverse_lazy('genres_lst')



