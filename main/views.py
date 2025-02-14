from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Article, ArticleSeries
from site_set.models import *
from etkinlikler.models import *
import base64
import hashlib
import hmac
import json
import random
import requests
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

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

def send_notification(ip):
    try:
        if not etkinlik_bildirimi.objects.filter(etkinlik_url=ip).exists():
            bildirim = etkinlik_bildirimi.objects.create(
                etkinlik_url=ip,
                bildirim_tarihi=timezone.now(),
                bildirim_mesaji="Sitemize hoş geldiniz! Yeni etkinlikler ve duyurular için bizi takip edin.",
                etkinlik=None
            )
            # Here you can add code to send the notification, e.g., via email or a messaging service
            print(f"Bildirim gönderildi: {bildirim.bildirim_mesaji}")
    except IntegrityError as e:
        print(f"IntegrityError: {e}")

# Create your views here.
def homepage(request):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    content["son_3_etkinlik"] = etkinlikler.objects.all().order_by('-etkinlik_tarihi')[:3]
    content["etkinlikler"]  = etkinlikler.objects.all().order_by('-etkinlik_tarihi')
    content["son_3_duyuru"] = Article.objects.all().order_by('-published')[:3]
    content["client_ip"] = client_ip
    return render(
        request=request,
        template_name='sayfalar/index.html',
        context=content
        )

def etkinlikler_sayfasi(request):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    etkinlik_list = etkinlikler.objects.all().order_by('-etkinlik_tarihi')
    paginator = Paginator(etkinlik_list, 10)  # Show 10 events per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content["page_obj"] = page_obj
    content["client_ip"] = client_ip
    return render(request, 'sayfalar/etkinlikler.html', context=content)

def duyurular(request):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    content["duyuru_kategorileri"] = ArticleSeries.objects.all()
    if request.GET.get("kategori"):
        content["duyurular"] = Article.objects.filter(series__slug=request.GET.get("kategori")).order_by('-published')[:15]
    else:
        content["duyurular"] = Article.objects.all().order_by('-published')[:15]
    content["client_ip"] = client_ip
    return render(request, 'sayfalar/duyurular.html', context=content)

def duyuru_detay(request, series_slug, article_slug):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    content["duyuru"] = Article.objects.get(series__slug=series_slug, article_slug=article_slug)
    content["client_ip"] = client_ip
    return render(request, 'sayfalar/duyuru_detay.html', context=content)

def etkinlik_detay(request, etkinlik_id, slug):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    content["etkinlik"] = get_object_or_404(etkinlikler, id=etkinlik_id)
    content["client_ip"] = client_ip
    return render(request, 'sayfalar/etkinlik_detay.html', context=content)

def galeri(request):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    etkinlik_list = resimler.objects.all()
    paginator = Paginator(etkinlik_list, 10)  # Show 10 events per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content["page_obj"] = page_obj
    content["client_ip"] = client_ip
    return render(request, 'sayfalar/galeri.html', context=content)

def iletisimm(request):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    content["client_ip"] = client_ip
    return render(request, 'sayfalar/iletisim.html', context=content)

def hakkimizdaa(request):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    content["client_ip"] = client_ip
    return render(request, 'sayfalar/hakkimizda.html', context=content)


def sepet(request):
    content = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    content["client_ip"] = client_ip
    
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
                content["error"] = "All fields are required."
                return render(request, 'sayfalar/sepet.html', context=content)
            
            a = etkinlik_sepeti.objects.create(
                etkinlik=etkinlik,
                katilimci=f"{name} {surname}",
                katilimci_email=email,
                katilimci_telefon=phone,
                toplam_fiyat=total_price,
                elden_satis_yapilan_ip=client_ip
            )
            
            if selected_seats:
                for i in selected_seats.split(","):
                    sepet_koltuk.objects.create(etkinlik_sepeti=a, koltuk_no=i)
            else:
                for i in range(1, int(quantity) + 1):
                    sepet_koltuk.objects.create(etkinlik_sepeti=a, koltuk_no=i)
            
            if request.user.is_superuser:
                etkinlik_sepeti.objects.filter(id=a.id).update(satin_alama_durumu=True, satin_alma_tarihi=timezone.now(), elden_satis=True)
                messages.success(request, "Satın Alma Başarılı (Admin)")
                return redirect("main:homepage")
            else:
                return redirect("main:payment")
    
    content["sepet"] = etkinlik_sepeti.objects.filter(elden_satis_yapilan_ip=client_ip)
    return render(request, 'sayfalar/sepet.html', context=content)

@csrf_exempt
def callback(request):
    return HttpResponse(str('OK'))

def success(request):
    context = dict()
    a = etkinlik_sepeti.objects.filter(satin_alama_durumu = False, elden_satis_yapilan_ip = get_client_ip(request)).last()
    etkinlik_sepeti.objects.filter(id = a.id).update(satin_alama_durumu = True, satin_alma_tarihi = timezone.now())
    messages.success(request, f"Satın Alma Başarılı")
    return redirect("/")

def fail(request):
    context = dict()
    context['fail'] = 'İşlem Başarısız'
    messages.success(request, f"Bundle Purchase Failed")
    return HttpResponse("Bundle Purchase Failed")

def home(request):
    sozluk = site_ayarlar()
    client_ip = get_client_ip(request)
    send_notification(client_ip)
    merchant_id = "541050"
    merchant_key = "QibXaYCYBac138za"
    merchant_salt = "XxTeSrRGjacxSt3x"
    merchant_ok_url = "http://127.0.0.1:8000/pay/out/success/"
    merchant_fail_url = 'http://127.0.0.1:8000/pay/out/failure/'
    sepet_bilgisi = etkinlik_sepeti.objects.filter(satin_alama_durumu = False, elden_satis_yapilan_ip = client_ip).last()
    merchant_oid =  str(random.randint(1, 9999999)) + "ID" + str(sepet_bilgisi.id)
    toplam_fiyat = sepet_bilgisi.toplam_fiyat
    sepetteki_urunler_getir = []
    bilgiler = sepet_koltuk.objects.filter(etkinlik_sepeti = sepet_bilgisi)
    for i in bilgiler:
        sepetteki_urunler_getir.append([str(i.koltuk_no), sepet_bilgisi.etkinlik.etkinlik_fiyati, 1])
    
    user_basket = base64.b64encode(json.dumps(sepetteki_urunler_getir).encode())
    test_mode = '1'
    debug_on = '1'

    # 3d'siz işlem
    non_3d = '0'

    # Ödeme süreci dil seçeneği tr veya en
    client_lang = "tr"

    # non3d işlemde, başarısız işlemi test etmek için 1 gönderilir (test_mode ve non_3d değerleri 1 ise dikkate alınır!)
    non3d_test_failed = '0'
    user_ip = str(client_ip)
    email = str(sepet_bilgisi.katilimci_email)

    # 100.99 TL ödeme
    payment_amount = str(int(toplam_fiyat) * 100)
    currency = 'TL'
    payment_type = 'card'
    user_name = str(sepet_bilgisi.katilimci)
    user_address = """Şerefiye, Kültür Sk.
No:16/3, 65100
İpekyolu/Van""" + " VAN" + " Türkiye"
    user_phone = str(sepet_bilgisi.katilimci_telefon)
    no_installment = "1"
    max_installment = "3"
    # Alabileceği değerler; advantage, axess, combo, bonus, cardfinans, maximum, paraf, world, saglamkart
    card_type = 'bonus'
    installment_count = '1'

    hash_str = merchant_id + user_ip + merchant_oid + email + payment_amount + user_basket.decode() + no_installment + max_installment + currency + test_mode
    paytr_token = base64.b64encode(hmac.new(merchant_key.encode(), (hash_str + merchant_salt).encode(), hashlib.sha256).digest())
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

        sozluk ['token'] = res['token']
        

    else:
        print(result.text)
    return render(request, 'odeme/payment.html', {"res": res, "content": sozluk})

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def custom_500(request):
    return render(request, '500.html', {}, status=500)
