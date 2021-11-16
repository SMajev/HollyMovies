from django import forms
from .models import Post, Category, Comment, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category')
        body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}))


class CommentForm(forms.ModelForm):
    queryset = User.objects.all()
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}))

    class Meta:
        model = Comment
        fields = ('body', )

