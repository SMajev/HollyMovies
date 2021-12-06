from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
from datetime import date

def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('First letter must be upper')

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    name = forms.CharField(max_length=128, validators=[capitalized_validator])


class PastMonthField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Past dates only')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = ('title', 'genre', 'rating', 'released', 'description', 'image')
        
    
    title = forms.CharField(max_length=128, validators=[capitalized_validator])
    genre = forms.ModelChoiceField(queryset=Genre.objects, required=False)
    rating = forms.FloatField(min_value=1, max_value=10)
    released = PastMonthField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}), required=False, )
    
    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()

        try:
            if result['genre'].name == 'Comedy' and result['rating'] > 5:
                self.add_error('genre', '')
                self.add_error('rating', '')
                raise ValidationError("Comedies aren't so good to be rated over 5.")
        except:
            pass
        return result
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CommentMovie(forms.ModelForm):
    class Meta:
        model = CommentMovieModel
        fields = ('body', )

    queryset = User.objects.all()
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}))
