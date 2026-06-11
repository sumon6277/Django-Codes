from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return HttpResponse("This is about page from practice app")

def contact(request):
    return HttpResponse("This is contact page from practice app")

def home(request):
    return HttpResponse("This is home page from practice app")