from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("etkinlikler/", views.etkinlikler_sayfasi, name="etkinlikler_sayfasi"),
    path("duyurular/", views.duyurular, name="duyurular"),
    path("duyurular/<slug:series_slug>/<slug:article_slug>/", views.duyuru_detay, name="duyuru_detay"),
    path("etkinlik_detay/<int:etkinlik_id>/<slug:slug>/", views.etkinlik_detay, name="etkinlik_detay"),
    path("galeri/", views.galeri, name="galeri"),
    path("iletisim/", views.iletisimm, name="iletisim"),
    path("hakkimizda/", views.hakkimizdaa, name="hakkimizda"),
]