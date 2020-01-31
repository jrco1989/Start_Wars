#from . import models
from film.models import Film, Personage, Planets
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

 
   
class PersonageForm(forms.Form):

    name_personage = forms.CharField(label='Nombre del personaje')
    actor = forms.CharField(label='Nombre del actor o actriz')
    performances= forms.ModelMultipleChoiceField(
        label='Peliculas',
        queryset=Film.objects.all(),
    )

    def create_personage(self):
        cleaned_data = super().clean()
        name_personage = cleaned_data.get('name_personage')
        actor = cleaned_data.get('actor')
        film_list = cleaned_data.get('performances')
        personage_obj = Personage.objects.create(name_personage=name_personage)
        for film in film_list:
            personage_obj.performances.add(film)

        personage_obj.save()
    
    class Meta:
        model = Personage
        fields = ['name_personage', 'actor','performances']

class PlanetsForm(forms.Form):

    name_planet = forms.CharField(label='Nombre del planeta')
    appearances= forms.ModelMultipleChoiceField(
        label='Peliculas',
        queryset=Film.objects.all(),
    )

    def create_planet(self):
        cleaned_data = super().clean()
        name_planet = cleaned_data.get('name_planet')
        film_list = cleaned_data.get('appearances')
        planet_obj = Planets.objects.create(name_planet=name_planet)
        
        for film in film_list:
            planet_obj.appearances.add(film)

        planet_obj.save()
    
    class Meta:
        model = Planets
        fields = ['name_planet', 'appearances']


