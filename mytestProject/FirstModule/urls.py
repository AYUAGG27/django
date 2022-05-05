from FirstModule import views
from django.urls import path


urlspatterns = [

    path('', views.firstModule, name='firstModule'),
    #path('aboutus', views.aboutus, name='aboutus')

]
