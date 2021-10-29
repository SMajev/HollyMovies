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

class CategoryPostsList(ListView):
    template_name = 'category_posts.html'
    model = Post
    context_object_name = 'category_posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        context["posts"] = context['posts'].filter(category__name=category)
        return context
    

class DetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'


