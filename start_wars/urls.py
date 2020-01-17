from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from film import views

urlpatterns = [
    path('admin/', 
        admin.site.urls),
    #path('',
     #   TemplateView.as_view(template_name='home.html'),
      #  name='home', )
    path(route='',view= views.home, name='home'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
