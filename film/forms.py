#from . import models
from film.models import Film, Personage
from django import forms


class FilmForm (forms.Form):

    """class Meta:
        model=Film
        fields=('title', 'opening_text', 'director')"""
    
    #title = forms.ChoiceField(choices=films, required=True, label="Seleccione la película")
    title=forms.CharField(label="Ingrese el título de la película")
    opening_text=forms.CharField(label="inserte el texto de apertura")
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

class PersonageForm(forms.Form):
#class TeamForm(forms.Form):
    name_personage = forms.CharField(label='Nombre del personaje')
    actor = forms.CharField(label='Nombre del actor o atriz')
    performances= forms.ModelMultipleChoiceField(
        label='Peliculas',
        queryset=Film.objects.all(),
    )

    def create_personage(self):
        cleaned_data = super().clean()
        name_personage = cleaned_data.get('name_personage')
        actor = cleaned_data.get('actor')
        film_list = cleaned_data.get('performances')
        team_obj = Personage.objects.create(name_personage=name_personage)
        for film in film_list:
            team_obj.performances.add(film)

        team_obj.save()
    
    class Meta:
        model = Personage
        fields = ['name_personage', 'actor','performances']
