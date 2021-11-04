from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from django.views import View
from django.views.generic import ListView, DetailView, DetailView, FormView
from django.views.generic.edit import ModelFormMixin, FormMixin
from django.urls import reverse, reverse_lazy
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
    paginate_by = 10

    def get_queryset(self):
        posts = super().get_queryset().filter(category__name=self.kwargs['cat'])
        return posts

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cat = self.kwargs['cat']
        context['cat_name'] = cat
        context['form'] = CommentForm
        return context
    
    

class DetailView(FormMixin, DetailView):
    template_name = 'post_detail.html'
    model = Post
    form_class = CommentForm
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['form'] = self.get_form()
        context['pk'] = self.object.pk
        context['comments'] = Comment.objects.filter(
            post=self.get_object()).order_by('-publish'
        )
        return context
    
    def post(self, request, *args, **kwargs):    
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('post', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        model_ins = form.save(commit=False)
        model_ins.post = self.get_object()
        model_ins.save()
        return super().form_valid(form)
        
    
class AddPostForm(FormView):
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/forum/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
  
class AddCommentForm(FormView):
    template_name = 'post_detail.html'
    form_class = CommentForm
    success_url = '/forum/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

