from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views
def index(request):
    return render(request, 'index.html')

def search(request):
    catalogue = Book.objects.all()
    return render(request, 'search.html', {'catalogue' : catalogue})

