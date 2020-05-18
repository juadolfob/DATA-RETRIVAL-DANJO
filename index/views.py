from django.shortcuts import render 
import pprint
import serpscrap

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def result(request):
    
    keywords = ['example']
    
    config = serpscrap.Config()
    config.set('scrape_urls', False)
    
    scrap = serpscrap.SerpScrap()
    scrap.init(config=config.get(), keywords=keywords)
    results = scrap.run()
    
    for result in results:
        pprint.pprint(result)
       
    return HttpResponse("Hello, world. You're at the polls index.")
