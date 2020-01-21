#from . import models
from film.models import Film
from django import forms


class FilmForm (forms.ModelForm):

    class Meta:
        model=Film
        fields=('title', 'opening_text', 'director')
        