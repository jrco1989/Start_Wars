from django.shortcuts import render, redirect


"""def create_film(request):
    if request.method == 'POST':
        title= request.POST['title']
		director= request.POST['director']
        opening_text= request.POST['openning_text']
        save.film()
   """    
       
       
def home(request):
    return render (request=request, template_name="home.html")


        
