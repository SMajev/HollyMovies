from django import forms
from .models import *
from django.contrib.auth.models import User

class UserCreate(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')