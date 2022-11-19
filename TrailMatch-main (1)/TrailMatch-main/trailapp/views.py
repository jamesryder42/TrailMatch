
from msilib.schema import ListView
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Trail
from django.db.models import Q
from django.views.generic.list import ListView
from trailapp.models import Trail,User
from trailapp.serializers import TrailSerializer
from rest_framework import viewsets

class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

def home(request):
    return render(request, "../templates/hello/home.html")

def about(request):
    return render(request, "../templates/hello/about.html")

def contact(request):
    return render(request, "../templates/hello/contact.html")

def trails(request):
    dbTrails=Trail.objects.all()
    context={'dbTrails': dbTrails}
    return render(request,'../templates/hello/trails.html',context)

def display_1_trail(request):
    return render(request, 'display_1/display_1_trail.html')

def search(request):
    query = request.GET.get("q")
    object_list= Trail.objects.filter(
        Q(trail_name__icontains=query) | Q(difficulty__icontains=query)
        )
    context={'object_list':object_list}
    return render(request,'../templates/hello/search.html',context)

