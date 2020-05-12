from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {'description':'NULL'}
    return render(request, 'movies/index.html', context)