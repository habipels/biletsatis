from django import template
from etkinlikler.models import *
register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def add(value, arg):
    return value + arg

@register.simple_tag
def oturma_duzeni():
    deger =[]
    for i in range(1,138):
        if i == 1:
            deger.append("-1") 
        
        elif i == 7:
            deger.append("-2") 
        elif i == 13:
           deger.append("-1") 
        elif i == 25:
           deger.append("-1")
        elif (i-25) % 15 == 0 and i >24  :
            deger.append("-1")        
        deger.append(i)

    return deger

@register.simple_tag
def etkinlik_koltuk_satin_alinma_durumu(etkinlik_id,koltuk_no):
    etkinlik = etkinlikler.objects.get(id=etkinlik_id)
    koltuk = sepet_koltuk.objects.filter(etkinlik_sepeti__etkinlik=etkinlik,koltuk_no=koltuk_no,etkinlik_sepeti__satin_alama_durumu = True)
    if koltuk:
        return True
    else:
        return False

@register.simple_tag
def koltuk_fiyati(etkinlik_id, koltuk_no):
    etkinlik = etkinlikler.objects.get(id=etkinlik_id)
    fiyat = etkinlik_koltuk_fiyaatlari.objects.filter(etkinlik=etkinlik, koltuk_no__lte=koltuk_no).order_by('-koltuk_no').first()
    if fiyat:
        return fiyat.fiyat
    else:
        return etkinlik.etkinlik_fiyati