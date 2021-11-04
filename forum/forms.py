from django import forms
from .models import Post, Category, Comment, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'category')
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    queryset = User.objects.all()
    author = forms.ModelChoiceField(queryset=queryset, widget=forms.Select)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}))

    class Meta:
        model = Comment
        fields = ('author', 'body', )
        


class EmailPostForm(forms.ModelForm):
    class Meta:

        fields = ('name', 'email', 'to', 'comments')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'to': forms.EmailInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'})
        }
    
    