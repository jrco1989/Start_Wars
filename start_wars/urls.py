from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from film import views

app_name = 'film'
urlpatterns = [
    path('admin/', 
        admin.site.urls),
    #path('',
    #   TemplateView.as_view(template_name='home.html'),
    #  name='home', )
    path(route='',
        view= views.home, 
        name='home'),
    path(
        route='films_list/',
        view= views.films_list,
        name='films_list'),
    path(route= 'film_detail/<int:pk>/',
        view=views.FilmDetail.as_view(template_name='film_detail.html'),
        name='film_detail'),
    path(
        'film_delete/<int:pk>/',
        views.FilmDelete.as_view(template_name='film_delete.html'),
        name='team_delete'),
    #path(route='film_create/', view=views.CreateFilm, name='film_create'),
    path(
        'film_create/',
        views.CreateFilm.as_view(),
        name='film_create'),
    
    
    path(route='personages_list/',
        view=views.PersonagesList.as_view(template_name='personages_list.html'),
        name='personages_list'),
    path(route= 'personage_detail/<int:pk>/',
        view=views.PersonageDetail.as_view(template_name='personage_detail.html'),
        name='personage_detail'),
    path(
        'personage_delete/<int:pk>/',
        views.PersonageDelete.as_view(template_name='personage_delete.html'),
        name='personage_delete'),
    path(
        'personage_create/',
        views.CreatePersonage.as_view(),
        name='personage_create'),
    
    
    path(route='planets_list/',
        view=views.PlanetsList.as_view(template_name='planets_list.html'),
        name='planets_list'),
    path(
        'planet_delete/<int:pk>/',
        views.PlanetDelete.as_view(template_name='planet_delete.html'),
        name='planet_delete'),
    path(
        'planet_create/',
        views.CreatePlanet.as_view(),
        name='planet_create'),

  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""path(route='film_detail/<int:pk>/', views.Film_Detail.as_view(template_name='film_detail.html'),
        name='film_detail',
    ),
    
      path('film_create/',
    view=views.CreateFilm.as_view(templeta_name='film_create.html'),
    name='film_create')"""