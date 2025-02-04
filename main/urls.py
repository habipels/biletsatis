from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("etkinlikler/", views.etkinlikler, name="etkinlikler"),
    path("duyurular/", views.duyurular, name="duyurular"),

]