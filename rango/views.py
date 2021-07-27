from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   html ='<a href="/rango/about/">About</a>'
   return HttpResponse(html + "Rango says hey there partner! ")

def about(request):
   html ='<a href="/rango/">Index</a>'
   return HttpResponse(html + "Rango says here is the about page.")