from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def secondModule(request):
    context={'text':"WELCOME HOME PAGE"}
    return render(request,'secondHome.html',secondModule)
     #return HttpResponse("SECOND MODULE HOME PAGE")
     
def aboutus(request):
         context={'text':'ABOUT US PAGE'}
         return render(request,'SecondAboutUS.html',secondModule)
         return HttpResponse("SECOND MODULE ABOUT US PAGE")
         
