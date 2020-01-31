from django.contrib import admin
from .models import Film, Personage, Planets


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title','director')
    #fields = ('title','director')
    #date_hierarchy = 'pub_date' pendiente d euso para cuando se añada la vista de edición, hay que crear el campo de pub_date 
class FilmAdmin(admin.ModelAdmin):
        exclude=('opening_text')    
    
@admin.register(Personage)
class PersonageAdmin(admin.ModelAdmin):
    list_display=('name_personage', 'actor')

@admin.register(Planets)
class PlanetsAdmin(admin.ModelAdmin):
    list_display=('name_planet',)
