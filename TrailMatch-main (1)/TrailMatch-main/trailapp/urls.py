from django.urls import path, include
from trailapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'everyTrail', views.TrailViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("trails/",views.trails,name="trails"),
    path("search/",views.search,name="search"),
    path('', include(router.urls)),
]

