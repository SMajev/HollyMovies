from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserForm, CustomPasswd, UserAdminForm, UserRegisterForm, AdminPasswd
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


class UsersList(PermissionRequiredMixin, ListView):
    template_name = 'account/users.html'
    model = User
    context_object_name = 'users'
    permission_required = 'auth.view_user'


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
    group_required = 'Users'
    success_url = reverse_lazy('index')


class UserUpdateView(UpdateView):
    template_name = 'registration/user_form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')

    def get_object(self):
        return User.objects.get(pk=self.kwargs['pk'])


class UserAdminView(PermissionRequiredMixin, SudoRequiredMixin, UserUpdateView):
    form_class = UserAdminForm  
    permission_required = 'auth.change_user'  


class CustomUserDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'account/user_delete.html'
    model = User
    success_url = reverse_lazy('users')
    permission_required = 'login.change_profile'


class SubmitablePasswordView(auth_views.PasswordChangeView):
    template_name = 'registration/user_passwd.html'
    success_url = reverse_lazy('index')
    form_class = CustomPasswd


class AdminPasswordView(PermissionRequiredMixin, auth_views.PasswordChangeView):
    model = User
    template_name = 'registration/admin_password.html'
    success_url = reverse_lazy('index')
    form_class = AdminPasswd
    permission_required = 'login.change_profile'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = User.objects.get(pk=self.kwargs['pk'])
        return kwargs

