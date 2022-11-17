
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


# Replace the existing home function with the one below
# def home(request):
#     return render(request, "../templates/hello/home.html")

def homepage(request):
    return render(request, "../templates/homepage.html")

def about(request):
    return render(request, "../templates/about.html")

def contact(request):
    return render(request, "../templates/contact.html")

def hello_there(request, name):
    return render(
        request,
        '../templates/hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

#print("http://127.0.0.1:8000/hello/James")
