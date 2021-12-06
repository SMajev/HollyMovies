from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your username'
    }))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Your email'
    }))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your first name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your last name'
    }))

class CustomPasswd(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'