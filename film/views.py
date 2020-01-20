from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Film
from django.views.generic import DetailView


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
    f=Film.objects.all().order_by('title')
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
