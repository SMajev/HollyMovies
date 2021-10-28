from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie, Genre

def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html', 
        context={'adjectives': [s0, s1, 'beautiful', 
        'wonderful']}
    )


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

