
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


def homepage(request):
    return render(request, "../templates/homepage.html")

def about(request):
    return render(request, "../templates/about.html")

def contact(request):
    return render(request, "../templates/contact.html")

# OLD CODE: just here for reference
# def hello_there(request, name):
#     return render(
#         request,
#         '../templates/hello/hello_there.html',
#         {
#             'name': name,
#             'date': datetime.now()
#         }
#     )
