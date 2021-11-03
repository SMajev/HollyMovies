from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from django.views import View
from django.views.generic import ListView, DetailView, DetailView, FormView
from .models import Category, Post, Comment
from .forms import EmailPostForm, PostForm, CommentForm

class CategoryList(ListView):
    template_name = 'categorys.html'
    model = Category
    context_object_name = 'categorys'


class CategoryPostsList(ListView):
    template_name = 'posts.html'
    model = Post
    context_object_name = 'posts'
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post=self.get_object()).order_by('-publish')
        context['comments'] = comments_connected
        return context
    
    
class AddPostForm(FormView):
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/forum/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    

class ShareForm(FormView):
    model = Post
    form_class = EmailPostForm
    success_url = 'email_share'

