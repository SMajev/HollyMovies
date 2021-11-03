from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from django.views import View
from django.views.generic import ListView, DetailView, DetailView, FormView
from .models import Category, Post
from .forms import EmailPostForm

class CategoryList(ListView):
    template_name = 'categorys.html'
    model = Category
    context_object_name = 'categorys'

class PostsList(ListView):
    template_name = 'posts.html'
    model = Post
    context_object_name = 'posts'

class CategoryPostsList(PostsList):
    def get(self, request, cat):
        category_posts = Post.objects.filter(category__name=cat)
        print(category_posts)
        context = {
            'posts': category_posts
        }
        return render(request, 'posts.html', context)
    

class DetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'
    
class ShareForm(FormView):
    def post(request, pk):
        post = get_object_or_404(Post, id=pk, status='published')

        if request.method == 'POST':
            form = EmailPostForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
        else:
            form = EmailPostForm()

        return render(
            request, 'share.html', {
            'post': post,
            'form': form
        })

