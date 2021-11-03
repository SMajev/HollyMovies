from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from django.views.generic import ListView, DetailView, DetailView
from .models import Category, Post

class CategoryList(ListView):
    template_name = 'categorys.html'
    model = Category
    context_object_name = 'categorys'

class PostsList(ListView):
    template_name = 'posts.html'
    model = Post
    context_object_name = 'posts'

class CategoryPostsList(View):
    model = Post
    def get(self, request, cat):
        category_posts = Post.objects.filter(category__name=cat)
        print(category_posts)
        context = {
            'category_posts': category_posts
        }
        return render(request, 'category_posts.html', context)
    

class DetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'


