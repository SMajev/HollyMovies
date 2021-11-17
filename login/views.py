from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView
from django.views.generic.edit import UpdateView
from forum.models import User
from .forms import UserCreate
from logging import getLogger

LOGGER = getLogger()

class ProfileView(DetailView):
    template_name = 'account/profile.html'
    model = User
    context_object_name = 'user'

class UserCreateView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreate
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        User.objects.create(
            username = cleaned_data['username'],
            password = cleaned_data['password'],
            email = cleaned_data['email'],
        )
        return result

    def form_invalid(self, form):
         LOGGER.warnings('User provides wrong data.')
         return super().form_invalid(form)

class UserUpdateView(UpdateView):
    template_name = 'registration/register.html'
    model = User
    form_class = UserCreate
    success_url = reverse_lazy('index')
    
    
    
