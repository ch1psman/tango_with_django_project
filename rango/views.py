from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   html =" <a href='/rango/about/'>About</a><br>"
   return HttpResponse(html + '\n'+"Rango says hey there partner! ")

def about(request):
   html ="<a href='/rango'>Index</a><br>"
   return HttpResponse(html + '\n'+"Rango says here is the about page.")