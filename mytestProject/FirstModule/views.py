from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def firstmodule(request):
    return HttpResponse("WELCOME TO CU")
    