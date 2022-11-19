from django.urls import path
from trailapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("trails/",views.trails,name="trails"),
    path("search/",views.search,name="search")
]

