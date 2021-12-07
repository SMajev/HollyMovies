from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, CreateView, ListView
from django.views.generic.edit import UpdateView
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserForm, CustomPasswd
from logging import getLogger
from django.contrib.auth import views as auth_views

LOGGER = getLogger()

class UsersList(ListView):
    template_name = 'account/users.html'
    model = User
    context_object_name = 'users'


class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'registration/log_out.html'

class ProfileView(DetailView):
    template_name = 'account/profile.html'
    model = User
    context_object_name = 'user'

class UserCreateView(CreateView):
    template_name = 'registration/user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

class UserUpdateView(UpdateView):
    template_name = 'registration/user_form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('index')
    
class SubmitablePasswordView(auth_views.PasswordChangeView):
    template_name = 'registration/user_passwd.html'
    success_url = reverse_lazy('index')
    form_class = CustomPasswd
