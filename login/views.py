from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from forum.models import User


class ProfileView(DetailView):
    template_name = 'account/profile.html'
    model = User
    context_object_name = 'user'


     
    
    
    
