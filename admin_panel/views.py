from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from .forms import (
    SayfaLogosuForm, SayfaIconuForm, SiteAdiForm, NumaraForm, AdresForm, 
    EmailAdresForm, SosyalMedyaTwForm, SosyalMedyaFbForm, SosyalMedyaInsgrForm, 
    BannerForm, HakkimizdaForm, IletisimForm, ResimlerForm, AciklamaForm
)
from site_set.models import (
    sayfa_logosu, sayfa_iconu, site_adi, numara, adres, email_adres, 
    sosyalmedyaTw, sosyalmedyafb, sosyalmedyaInsgr, banner, hakkimizda, 
    iletisim, resimler, aciklama
)

MODEL_FORM_MAPPING = {
    'sayfa_logosu': (sayfa_logosu, SayfaLogosuForm),
    'sayfa_iconu': (sayfa_iconu, SayfaIconuForm),
    'site_adi': (site_adi, SiteAdiForm),
    'numara': (numara, NumaraForm),
    'adres': (adres, AdresForm),
    'email_adres': (email_adres, EmailAdresForm),
    'sosyalmedyaTw': (sosyalmedyaTw, SosyalMedyaTwForm),
    'sosyalmedyafb': (sosyalmedyafb, SosyalMedyaFbForm),
    'sosyalmedyaInsgr': (sosyalmedyaInsgr, SosyalMedyaInsgrForm),
    'banner': (banner, BannerForm),
    'hakkimizda': (hakkimizda, HakkimizdaForm),
    'iletisim': (iletisim, IletisimForm),
    'resimler': (resimler, ResimlerForm),
    'aciklama': (aciklama, AciklamaForm),
}

def admin_homepage(request):
    return render(request, 'admin_panel/index.html')

@user_passes_test(lambda u: u.is_superuser)
def list_models(request):
    context = {
        'sayfa_logosu': sayfa_logosu.objects.all(),
        'sayfa_iconu': sayfa_iconu.objects.all(),
        'site_adi': site_adi.objects.all(),
        'numara': numara.objects.all(),
        'adres': adres.objects.all(),
        'email_adres': email_adres.objects.all(),
        'sosyalmedyaTw': sosyalmedyaTw.objects.all(),
        'sosyalmedyafb': sosyalmedyafb.objects.all(),
        'sosyalmedyaInsgr': sosyalmedyaInsgr.objects.all(),
        'banner': banner.objects.all(),
        'hakkimizda': hakkimizda.objects.all(),
        'iletisim': iletisim.objects.all(),
        'resimler': resimler.objects.all(),
        'aciklama': aciklama.objects.all(),
    }
    return render(request, 'admin_panel/list_models.html', context)

@user_passes_test(lambda u: u.is_superuser)
def create_model(request, model_name):
    model, model_form = MODEL_FORM_MAPPING[model_name]
    if request.method == 'POST':
        form = model_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_models')
    else:
        form = model_form()
    return render(request, 'admin_panel/create_model.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def update_model(request, model_name, pk):
    model, model_form = MODEL_FORM_MAPPING[model_name]
    instance = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = model_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('list_models')
    else:
        form = model_form(instance=instance)
    return render(request, 'admin_panel/update_model.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_model(request, model_name, pk):
    model, _ = MODEL_FORM_MAPPING[model_name]
    instance = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('list_models')
    return render(request, 'admin_panel/confirm_delete.html', {'object': instance})

@user_passes_test(lambda u: u.is_superuser)
def list_social_media(request):
    context = {
        'sosyalmedyaTw': sosyalmedyaTw.objects.all(),
        'sosyalmedyafb': sosyalmedyafb.objects.all(),
        'sosyalmedyaInsgr': sosyalmedyaInsgr.objects.all(),
    }
    return render(request, 'admin_panel/list_social_media.html', context)

@user_passes_test(lambda u: u.is_superuser)
def create_social_media(request, model_name):
    model, model_form = MODEL_FORM_MAPPING[model_name]
    if request.method == 'POST':
        form = model_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_social_media')
    else:
        form = model_form()
    return render(request, 'admin_panel/create_social_media.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def update_social_media(request, model_name, pk):
    model, model_form = MODEL_FORM_MAPPING[model_name]
    instance = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = model_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('list_social_media')
    else:
        form = model_form(instance=instance)
    return render(request, 'admin_panel/update_social_media.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_social_media(request, model_name, pk):
    model, _ = MODEL_FORM_MAPPING[model_name]
    instance = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('list_social_media')
    return render(request, 'admin_panel/confirm_delete.html', {'object': instance})

@user_passes_test(lambda u: u.is_superuser)
def sosyal_medya_tw(request):
    content = {}
    content["sosyalmedyaTw"] = sosyalmedyaTw.objects.all()
    return render(request, 'admin_panel/sosyal_medya.html', content)

@user_passes_test(lambda u: u.is_superuser)
def sosyal_medya_fb(request):
    content = {}
    content["sosyalmedyafb"] = sosyalmedyafb.objects.all()
    return render(request, 'admin_panel/sosyal_medya.html', content)

@user_passes_test(lambda u: u.is_superuser)
def sosyal_medya_insgr(request):
    content = {}
    content["sosyalmedyaInsgr"] = sosyalmedyaInsgr.objects.all()
    return render(request, 'admin_panel/sosyal_medya.html', content)

@user_passes_test(lambda u: u.is_superuser)
def sayfa_logosu_view(request):
    content = {}
    content["sayfa_logosu"] = sayfa_logosu.objects.all()
    return render(request, 'admin_panel/sayfa_logosu.html', content)

@user_passes_test(lambda u: u.is_superuser)
def sayfa_iconu_view(request):
    content = {}
    content["sayfa_iconu"] = sayfa_iconu.objects.all()
    return render(request, 'admin_panel/sayfa_iconu.html', content)

@user_passes_test(lambda u: u.is_superuser)
def site_adi_view(request):
    content = {}
    content["site_adi"] = site_adi.objects.all()
    return render(request, 'admin_panel/site_adi.html', content)

@user_passes_test(lambda u: u.is_superuser)
def numara_view(request):
    content = {}
    content["numara"] = numara.objects.all()
    return render(request, 'admin_panel/numara.html', content)

@user_passes_test(lambda u: u.is_superuser)
def adres_view(request):
    content = {}
    content["adres"] = adres.objects.all()
    return render(request, 'admin_panel/adres.html', content)

@user_passes_test(lambda u: u.is_superuser)
def email_adres_view(request):
    content = {}
    content["email_adres"] = email_adres.objects.all()
    return render(request, 'admin_panel/email_adres.html', content)

@user_passes_test(lambda u: u.is_superuser)
def banner_view(request):
    content = {}
    content["banner"] = banner.objects.all()
    return render(request, 'admin_panel/banner.html', content)

@user_passes_test(lambda u: u.is_superuser)
def hakkimizda_view(request):
    content = {}
    content["hakkimizda"] = hakkimizda.objects.all()
    return render(request, 'admin_panel/hakkimizda.html', content)

@user_passes_test(lambda u: u.is_superuser)
def iletisim_view(request):
    content = {}
    content["iletisim"] = iletisim.objects.all()
    return render(request, 'admin_panel/iletisim.html', content)

@user_passes_test(lambda u: u.is_superuser)
def resimler_view(request):
    content = {}
    content["resimler"] = resimler.objects.all()
    return render(request, 'admin_panel/resimler.html', content)

@user_passes_test(lambda u: u.is_superuser)
def aciklama_view(request):
    content = {}
    content["aciklama"] = aciklama.objects.all()
    return render(request, 'admin_panel/aciklama.html', content)