from django.shortcuts import render
from django.http import HttpResponse

#import Model Data
from .models import Aufgabe

# Create your views here.

def home(request):
    context = {
        'title': 'Home',
        'aufgaben': Aufgabe.objects.all()
    }
    return render(request, 'mainapp/home.html', context)