from django.urls import path
from . import views

urlpatterns = [
    path("", views.admin_homepage, name="admin_homepage"),
    path("list/", views.list_models, name="list_models"),
    path("create/<str:model_name>/", views.create_model, name="create_model"),
    path("update/<str:model_name>/<int:pk>/", views.update_model, name="update_model"),
    path("delete/<str:model_name>/<int:pk>/", views.delete_model, name="delete_model"),
    path("social_media/", views.list_social_media, name="list_social_media"),
    path("social_media/create/<str:model_name>/", views.create_social_media, name="create_social_media"),
    path("social_media/update/<str:model_name>/<int:pk>/", views.update_social_media, name="update_social_media"),
    path("social_media/delete/<str:model_name>/<int:pk>/", views.delete_social_media, name="delete_social_media"),
    path("sosyal_medya_tw/", views.sosyal_medya_tw, name="sosyal_medya_tw"),
    path("sosyal_medya_fb/", views.sosyal_medya_fb, name="sosyal_medya_fb"),
    path("sosyal_medya_insgr/", views.sosyal_medya_insgr, name="sosyal_medya_insgr"),
    path("sayfa_logosu/", views.sayfa_logosu_view, name="sayfa_logosu"),
    path("sayfa_iconu/", views.sayfa_iconu_view, name="sayfa_iconu"),
    path("site_adi/", views.site_adi_view, name="site_adi"),
    path("numara/", views.numara_view, name="numara"),
    path("adres/", views.adres_view, name="adres"),
    path("email_adres/", views.email_adres_view, name="email_adres"),
    path("banner/", views.banner_view, name="banner"),
    path("hakkimizda/", views.hakkimizda_view, name="hakkimizda"),
    path("iletisim/", views.iletisim_view, name="iletisim"),
    path("resimler/", views.resimler_view, name="resimler"),
    path("aciklama/", views.aciklama_view, name="aciklama"),
]