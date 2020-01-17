from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', 
        admin.site.urls),
    path('',
        TemplateView.as_view(template_name='home.html'),
        name='home', )
    #path(route='ingreso/',view= views.ingreso, name='ingreso'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
