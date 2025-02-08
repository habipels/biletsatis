from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Article, ArticleSeries
from site_set.models import *
from etkinlikler.models import *
merchant_id = "541050"
merchant_key = "QibXaYCYBac138za"
merchant_salt = "XxTeSrRGjacxSt3x"
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

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
    sozluk["now"] = timezone.now()
    return sozluk

# Create your views here.
def homepage(request):
    content = site_ayarlar()
    content["son_3_etkinlik"] = etkinlikler.objects.all().order_by('-etkinlik_tarihi')[:3]
    content["etkinlikler"]  = etkinlikler.objects.all().order_by('-etkinlik_tarihi')
    content["client_ip"] = get_client_ip(request)
    return render(
        request=request,
        template_name='sayfalar/index.html',
        context=content
        )

def etkinlikler_sayfasi(request):
    content = site_ayarlar()
    etkinlik_list = etkinlikler.objects.all().order_by('-etkinlik_tarihi')
    paginator = Paginator(etkinlik_list, 10)  # Show 10 events per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content["page_obj"] = page_obj
    content["client_ip"] = get_client_ip(request)
    return render(request, 'sayfalar/etkinlikler.html', context=content)

def duyurular(request):
    content = site_ayarlar()
    content["duyuru_kategorileri"] = ArticleSeries.objects.all()
    if request.GET.get("kategori"):
        content["duyurular"] = Article.objects.filter(series__slug=request.GET.get("kategori")).order_by('-published')[:15]
    else:
        content["duyurular"] = Article.objects.all().order_by('-published')[:15]
    content["client_ip"] = get_client_ip(request)
    return render(request, 'sayfalar/duyurular.html', context=content)

def duyuru_detay(request, series_slug, article_slug):
    content = site_ayarlar()
    content["duyuru"] = Article.objects.get(series__slug=series_slug, article_slug=article_slug)
    content["client_ip"] = get_client_ip(request)
    return render(request, 'sayfalar/duyuru_detay.html', context=content)

def etkinlik_detay(request, etkinlik_id, slug):
    content = site_ayarlar()
    content["etkinlik"] = get_object_or_404(etkinlikler, id=etkinlik_id)
    content["client_ip"] = get_client_ip(request)
    return render(request, 'sayfalar/etkinlik_detay.html', context=content)

def galeri(request):
    content = site_ayarlar()
    etkinlik_list = resimler.objects.all()
    paginator = Paginator(etkinlik_list, 10)  # Show 10 events per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content["page_obj"] = page_obj
    content["client_ip"] = get_client_ip(request)
    return render(request, 'sayfalar/galeri.html', context=content)

def iletisimm(request):
    content = site_ayarlar()
    content["client_ip"] = get_client_ip(request)
    return render(request, 'sayfalar/iletisim.html', context=content)

def hakkimizdaa(request):
    content = site_ayarlar()
    content["client_ip"] = get_client_ip(request)
    return render(request, 'sayfalar/hakkimizda.html', context=content)

def sepet(request):
    content = site_ayarlar()
    content["client_ip"] = get_client_ip(request)
    
    if request.method == "POST":
        if not request.POST.get("name"):
            if request.POST.get("etkinlik_id"):
                content["etkinlik"] = request.POST.get("etkinlik_id")
            if request.POST.get("selected_seats"):
                content["selected_seats"] = request.POST.get("selected_seats")
            if request.POST.get("quantity"):
                content["quantity"] = request.POST.get("quantity")
            if request.POST.get("total_price"):
                content["total_price"] = request.POST.get("total_price")
        else:
            etkinlik_id = request.POST.get('etkinlik_id')
            etkinlik = get_object_or_404(etkinlikler, id=etkinlik_id)
            selected_seats = request.POST.get('selected_seats')
            quantity = request.POST.get('quantity')
            total_price = request.POST.get('total_price')
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            
            if not (name and surname and phone and email):
                # Handle the case where required fields are missing
                content["error"] = "All fields are required."
                return render(request, 'sayfalar/sepet.html', context=content)
            
            a = etkinlik_sepeti.objects.create(
                etkinlik=etkinlik,
                katilimci=f"{name} {surname}",
                katilimci_email=email,
                katilimci_telefon=phone,
                toplam_fiyat=total_price,
                elden_satis_yapilan_ip=get_client_ip(request)
            )
            
            if selected_seats:
                for i in selected_seats.split(","):
                    sepet_koltuk.objects.create(etkinlik_sepeti=a, koltuk_no=i)
            else:
                for i in range(1, int(quantity) + 1):
                    sepet_koltuk.objects.create(etkinlik_sepeti=a, koltuk_no=i)
            # Process the form data as needed
            # For example, save the order to the database or send a confirmation email
            # ...
        
    content["sepet"] = etkinlik_sepeti.objects.filter(elden_satis_yapilan_ip=get_client_ip(request))
    return render(request, 'sayfalar/sepet.html', context=content)
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib import messages
import pprint
from django.shortcuts import render, redirect,get_object_or_404
import json
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
import base64
import hashlib
import hmac
import html
import json
import random

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def callback(request):
    return HttpResponse(str('OK'))


def success(request):
    context = dict()
   
    messages.success(request, f"Satın Alma Başarılı")
    return redirect("/")


def fail(request):
    context = dict()
    context['fail'] = 'İşlem Başarısız'

    messages.success(request, f"Bundle Purchase Failed")
    return HttpResponse("Bundle Purchase Failed")

def home(request):
    sozluk = site_ayarlar()
    merchant_ok_url = "https://humanbilet.com/pay/out/success/"
    merchant_fail_url = 'https://humanbilet.com/pay/out/failure/'
    context = dict()
    if request.user.is_authenticated:
        ads =sepet_sahibi_bilgileri.objects.filter(kayitli_kullanici = sepet_olusturma.objects.filter(sepet_sahibi = request.user,sepet_satin_alma_durumu = False).last()).last()
        user_sepet = sepet_olusturma.objects.filter(sepet_sahibi = request.user,sepet_satin_alma_durumu = False).last()
        sepetteki_urunler_getir = []
        a = sepetteki_urunler.objects.filter(kayitli_kullanici = user_sepet)
        toplam_fiyat = 0
        for i in a:
            if i.urun_adedi > 0:
                sepetteki_urunler_getir.append([str(i.urun_bilgisi.urun_adi),str(i.urun_bilgisi.fiyat),int(i.urun_adedi)])
                toplam_fiyat = toplam_fiyat+ (float(i.urun_bilgisi.fiyat)*int(i.urun_adedi))
        merchant_oid =bugunsiparis()+'OS' + random.randint(1, 9999999).__str__()+"ID"+ str(user_sepet.id)
    else:
        ads = get_object_or_404(sepet_sahibi_bilgileri,kayitli_olmayan_kullanici = sepet_olusturma_ip.objects.filter(sepet_sahibi = get_client_ip(request),sepet_satin_alma_durumu = False).last())
        user_sepet = sepet_olusturma_ip.objects.filter(sepet_sahibi = get_client_ip(request),sepet_satin_alma_durumu = False).last()
        sepetteki_urunler_getir = []
        a = sepetteki_urunler.objects.filter(kayitli_olmayan_kullanici = user_sepet)
        toplam_fiyat = 0
        for i in a:
            if i.urun_adedi > 0:
                sepetteki_urunler_getir.append([str(i.urun_bilgisi.urun_adi),str(i.urun_bilgisi.fiyat),int(i.urun_adedi)])
                toplam_fiyat = toplam_fiyat+ (float(i.urun_bilgisi.fiyat)*int(i.urun_adedi))
        merchant_oid =bugunsiparis()+'OS' + random.randint(1, 9999999).__str__()+"KayitsizID"+ str(user_sepet.id)
    user_basket = base64.b64encode(json.dumps(sepetteki_urunler_getir).encode())


    test_mode = '1'
    debug_on = '1'

    # 3d'siz işlem
    non_3d = '0'

    # Ödeme süreci dil seçeneği tr veya en
    client_lang = "tr"

    # non3d işlemde, başarısız işlemi test etmek için 1 gönderilir (test_mode ve non_3d değerleri 1 ise dikkate alınır!)
    non3d_test_failed = '0'
    user_ip = str(get_client_ip(request))
    email = str(ads.email)

    # 100.99 TL ödeme

    payment_amount = str(int(toplam_fiyat)*100)
    currency = 'TL'
    payment_type = 'card'
    user_name = str(ads.isim)+" "+ str(ads.soyisim)
    user_address = str(ads.adres) + " "+str(ads.sehirler)+" "+str(ads.ulke)
    user_phone = str(ads.telefon)
    no_installment = "1"
    max_installment="3"
    # Alabileceği değerler; advantage, axess, combo, bonus, cardfinans, maximum, paraf, world, saglamkart
    card_type = 'bonus'
    installment_count = '1'

    hash_str = merchant_id + user_ip + merchant_oid + email + payment_amount + user_basket.decode()+ no_installment + max_installment + currency + test_mode
    paytr_token = base64.b64encode(hmac.new(merchant_key, hash_str.encode() + merchant_salt, hashlib.sha256).digest())
    context = {
        'merchant_id': merchant_id,
        'user_ip': user_ip,
        'merchant_oid': merchant_oid,
        'email': email,
        'payment_type': payment_type,
        'payment_amount': payment_amount,
        'currency': currency,
        'test_mode': test_mode,
        'non_3d': non_3d,
        'merchant_ok_url': merchant_ok_url,
        'merchant_fail_url': merchant_fail_url,
        'user_name': user_name,
        'user_address': user_address,
        'user_phone': user_phone,
        'user_basket': user_basket.decode(),
        'debug_on': debug_on,
        'no_installment': no_installment,
        'max_installment': max_installment,
        'client_lang': client_lang,
        'paytr_token': paytr_token.decode(),
        'non3d_test_failed': non3d_test_failed,
        'installment_count': installment_count,
        'card_type': card_type,

    }
    result = requests.post('https://www.paytr.com/odeme/api/get-token', context)
    res = json.loads(result.text)

    if res['status'] == 'success':
        print(res['token'])
        print(result.text)


        content = {
            'token': res['token']
        }

    else:
        print(result.text)
    return render(request, 'odeme/payment.html',{"res":res,"content":sozluk})
