
from secondModule import views
from django.urls import path


urlspatterns = [
    
    path('',views.secondModule,name='secondModule'),
    path('aboutus',views.aboutus,name='aboutus')
    
]