from django.urls import path
from trailapp import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
