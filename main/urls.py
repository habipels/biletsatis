from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("etkinlikler/", views.etkinlikler_sayfasi, name="etkinlikler_sayfasi"),
    path("duyurular/", views.duyurular, name="duyurular"),
    path("etkinlik_detay/<int:etkinlik_id>/<slug:slug>/", views.etkinlik_detay, name="etkinlik_detay"),

]