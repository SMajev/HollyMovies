from django import forms
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AdminPasswordChangeForm
from django.db.transaction import atomic

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups']

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

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = forms.CharField(label='Your story',
                                    widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}),
                                    min_length=20
                                )
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
             
    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        user = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=user)
        if commit:
            profile.save()
        return user


class CustomPasswd(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AdminPasswd(AdminPasswordChangeForm):
    model = User
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'











# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         # fields = '__all__'

#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Your username'
#     }))
#     email = forms.CharField(widget=forms.EmailInput(
#         attrs={'class': 'form-control', 'placeholder': 'Your email'
#     }))
#     password1 = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Password'
#     }))
#     password2 = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Password Confirmed'
#     }))

#     def __init__(self, *args, **kwargs):
#         super().__init__(**kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

