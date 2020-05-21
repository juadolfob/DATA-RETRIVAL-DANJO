from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import re
import requests

def index(request):
    context = {'description':'NULL'}
    return render(request, 'movies/index.html', context)

def result(request):
    url = "https://www.whatismymovie.com/results?"
    html = requests.get(url,params={'text':request.GET['movie_description']}).Text
    regex = r"<a\s*href=[\"']item\?item=[0-9]*[\"']>.*?<\/a>" 
    regex_image = r"src='"
    html = re.sub(regex_image, "class='resize' src='https://www.whatismymovie.com", html)
    matches = re.findall(regex, html)
    
    pairmatches=[]
    dict={}
    for i,match in enumerate(matches):
        if i%2==0:
            dict={}
            dict['movie_name']=match
        else:
            dict['movie_image']=match
            pairmatches.append(dict)
    print(pairmatches)
    context = {'results':pairmatches}
    return render(request, 'movies/result.html', context)