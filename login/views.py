from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, CreateView, ListView
from django.views.generic.edit import UpdateView
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserForm, CustomPasswd, UserAdminForm, UserRegisterForm
from logging import getLogger
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
LOGGER = getLogger()


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class SudoRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class BothRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser, self.request.user.is_staff


class UsersList(PermissionRequiredMixin, BothRequiredMixin, ListView):
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
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')


class UserUpdateView(UpdateView):
    template_name = 'registration/user_form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('index')


class UserAdminView(PermissionRequiredMixin, SudoRequiredMixin, UserUpdateView):
    form_class = UserAdminForm    


class SubmitablePasswordView(auth_views.PasswordChangeView):
    template_name = 'registration/user_passwd.html'
    success_url = reverse_lazy('index')
    form_class = CustomPasswd
