from django import forms
from .models import Post, Category, Comment, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        prepopulated_fields = {'slug': ('title', )}
        widgets ={
            'author': forms.TextInput(attrs={'readonly': 'readonly'}),
            'slug': forms.TextInput(attrs={'readonly': 'readonly'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'cols': 60, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(PostForm).save(commit=False)
        obj.slug = slugify(self.title)
        obj.author = self.author
        if commit:
            obj.save()
        return obj

class CommentForm(forms.ModelForm):
    queryset = User.objects.all()
    author = forms.ModelChoiceField(queryset=queryset, widget=forms.Select)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}))

    class Meta:
        model = Comment
        fields = ('author', 'body', )

    def save(self, commit=True):
        obj = super(CommentForm).save(commit=False)
        if commit:
            obj.save()
        return obj
        


