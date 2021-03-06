
from . import models, forms
from.forms import FilmForm, PersonageForm, PlanetsForm
from .models import Film
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, DeleteView, CreateView, ListView
from django.views.generic.edit import FormView



"""def create_film(request):
    if request.method == 'POST':
        title= request.POST['title']
		director= request.POST['director']
        opening_text= request.POST['openning_text']
        save.film()
   """    
       
       
def home(request):
    return render (request=request, template_name="home.html")

def films_list(request):
    f=Film.objects.all().order_by('id')
    #return render(request, 'blog/post_list.html', {'posts': posts})
    return render (request=request, template_name="films_list.html",context={'f':f} )
    
"""def film_detail(request,pk):
    film = get_object_or_404(Film, pk=pk)
    #return render(request, 'blog/post_detail.html', {'post': post})
    return render (request=request, template_name='film_detail.html', context={'film':film})"""

class FilmDetail(DetailView):
    
    object = models.Film

    def get_object(self, queryset=None):
        return get_object_or_404(models.Film, id=self.kwargs['pk'])

class FilmDelete(DeleteView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.Film, pk=self.kwargs['pk'])

        if obj:
            obj.delete()
            return JsonResponse({'ok': True})

        return JsonResponse({'ok': False})

#class FilmEdith():

""""def CreateFilm(request):
    
    #if request.method =='POST':
        form=FilmForm(request.POST)
        if form.is_valid():
            film=form.save(commit=False)#commit false significa que aún no queremo sguardar el formulario
            film.save()
            return redirect('film_detail', pk=film.pk)"""

class CreateFilm(FormView):
    template_name = 'film_create.html'
    form_class = FilmForm
    success_url = '/film_create/'

    def form_valid(self, form):
        form.create_film()

        return super().form_valid(form)

class PersonagesList(ListView):
    model = models.Personage
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        queryset = models.Personage.objects.all()

        return queryset
class PersonageDetail(DetailView):
    
    object = models.Personage

    def get_object(self, queryset=None):
        return get_object_or_404(models.Personage, id=self.kwargs['pk'])

class PersonageDelete(DeleteView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.Personage, pk=self.kwargs['pk'])

        if obj:
            obj.delete()
            return JsonResponse({'ok': True})

        return JsonResponse({'ok': False})

class CreatePersonage(FormView):
    template_name = 'personage_create.html'
    form_class = PersonageForm
    success_url = '/personage_create/'

    def form_valid(self, form):
        form.create_personage()

        return super().form_valid(form)

class PlanetsList(ListView):
    model = models.Planets
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        queryset = models.Planets.objects.all()

        return queryset

class PlanetDelete(DeleteView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.Planets, pk=self.kwargs['pk'])

        if obj:
            obj.delete()
            return JsonResponse({'ok': True})

        return JsonResponse({'ok': False})

class CreatePlanet(FormView):
    template_name = 'planet_create.html'
    form_class = PlanetsForm
    success_url = '/planet_create/'

    def form_valid(self, form):
        form.create_planet()

        return super().form_valid(form)

