from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("etkinlikler_fiyat/", views.koltuk_fiyatlari_degistir_otomatik, name="koltuk_fiyatlari_degistir_otomatik"),
    path("etkinlikler_fiyat/<int:etkinlik_id>/<int:baslangic_koltuk>/<int:koltuk_no>/<int:fiyat>/", views.koltuk_fiyatlari_degistir_otomatik, name="koltuk_fiyatlari_degistir_otomatik"),
    path("etkinlikler/", views.etkinlikler_sayfasi, name="etkinlikler_sayfasi"),
    path("duyurular/", views.duyurular, name="duyurular"),
    path("duyurular/<slug:series_slug>/<slug:article_slug>/", views.duyuru_detay, name="duyuru_detay"),
    path("etkinlik_detay/<int:etkinlik_id>/<slug:slug>/", views.etkinlik_detay, name="etkinlik_detay"),
    path("galeri/", views.galeri, name="galeri"),
    path("iletisim/", views.iletisimm, name="iletisim"),
    path("hakkimizda/", views.hakkimizdaa, name="hakkimizda"),
    path("sepet/", views.sepet, name="sepet"),
    path('pay/out/payment/', views.home, name='payment'),
    path('pay/out/result/', views.callback, name='result'),
    path('pay/out/success/', views.success, name='success'),
    path('pay/out/failure/', views.fail, name='failure'),
]