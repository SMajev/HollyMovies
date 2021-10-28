from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Movie, Genre



class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie


# class MovieView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all()}


# class MovieView(View):
#     def get(self, request):
#         return render(
#             request, template_name='movies.html',
#             context={'movies': Movie.objects.all()}
#         )


def movies(request):
    sorting = request.GET.get('s', 'title')
    if sorting == 'title':
        movies_lst = Movie.objects.all().order_by('title')

    elif sorting == 'rating':
        movies_lst = Movie.objects.all().order_by('-rating')

    elif sorting == 'year':
        movies_lst = Movie.objects.all().order_by('realeased')

    else:
        movies_lst = Movie.objects.all()

    return render(
        request, template_name='movies.html',
        context={'movies': movies_lst}
    )


def genres(request):
    return render(
        request, template_name='genres.html',
        context={'genres': Genre.objects.all()}
    )

def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html', 
        context={'adjectives': [s0, s1, 'beautiful', 
        'wonderful']}
    )