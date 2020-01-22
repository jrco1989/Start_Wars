#from . import models
from film.models import Film, Personage
from django import forms


class FilmForm (forms.Form):

    """class Meta:
        model=Film
        fields=('title', 'opening_text', 'director')"""
    title = forms.CharField(label='Nombre de la película')
    opening_text=forms.CharField(help_text="insert the text opening")
    director = forms.CharField(label='Nombre del director')
    #personage = forms.ModelMultipleChoiceField(
     #   label='Personajes',
      #  queryset=Personage.objects.all(),
    

    def create_film(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        opening_text = cleaned_data.get('opening_text')
        director = cleaned_data.get('director')
        
        Film.objects.create(title=title,
                            opening_text=opening_text,
                            director=director,)
    
        #film_obj.save()

    """def update_team(self, pk):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        user_list = cleaned_data.get('user')
        team_obj = Team.objects.filter(pk=pk)
        team_obj.update(name=name)
        team_obj = team_obj.first()
        team_obj.user.clear()

        for user in user_list:
            team_obj.user.add(user)

        team_obj.save()

    """
    class Meta:
        model = Film
        fields = ['title', 'opening_text','director']