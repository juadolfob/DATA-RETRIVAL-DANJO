from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import settings

def index(request):
    apps=[app for app in settings.INSTALLED_APPS if not app.startswith("django.")]
    apps_dict=[]
    for i,app in enumerate(apps):
        app_dict={}
        _app_=app.split(".")
        exec("from "+_app_[0]+"."+_app_[1]+" import "+_app_[2])
        app_dict["name"]=(eval(_app_[2]+".name"))
        app_dict["description"]=(eval(_app_[2]+".description"))
        app_dict["image"]=(eval(_app_[2]+".image"))
        app_dict["image_caption"]=(eval(_app_[2]+".image_caption"))
        app_dict["body"]=(eval(_app_[2]+".body"))
        apps_dict.append(app_dict)
    context = {'apps':apps_dict}
    return render(request, 'recinfo/index.html', context)