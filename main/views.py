from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleSeries
from site_set.models import *

def site_ayarlar():
    sozluk= {}
    sozluk['site_adi'] = site_adi.objects.last()
    sozluk['numara'] = numara.objects.last()
    sozluk['adres'] = adres.objects.last()
    sozluk['email_adres'] = email_adres.objects.last()
    sozluk['sosyalmedyaTw'] = sosyalmedyaTw.objects.last()
    sozluk['sosyalmedyafb'] = sosyalmedyafb.objects.last()
    sozluk['sosyalmedyaInsgr'] = sosyalmedyaInsgr.objects.last()
    sozluk['banner'] = banner.objects.last()
    sozluk['hakkimizda'] = hakkimizda.objects.last()
    sozluk['iletisim'] = iletisim.objects.last()
    sozluk['resimler'] = resimler.objects.all()
    sozluk['aciklama'] = aciklama.objects.last()
    #sozluk["logo"] = sayfa_logosu.objects.last()
    sozluk["icon"] = sayfa_iconu.objects.last()
    return sozluk
# Create your views here.
def homepage(request):
    content = site_ayarlar()
    
    return render(
        request=request,
        template_name='sayfalar/index.html',
        context=content
        )

def etkinlikler(request):
    content = site_ayarlar()
    return render(request, 'sayfalar/etkinlikler.html', context=content)

def duyurular(request):
    content = site_ayarlar()
    return render(request, 'sayfalar/duyurular.html', context=content)