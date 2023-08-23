from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, word!")

def index(reqest):
    return HttpResponse("Hi, this is the index!")