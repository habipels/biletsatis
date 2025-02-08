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
    deger =["-4",1,2,3,4,5,6,"-2",13,14,15,16,17,18,"-1","-4",7,8,9,10,11,12,19,20,21,22,23,24,"-1"]
    
    for i in range(25,141):
        if i == 1:
            deger.append("-1") 
        
        elif i == 7:
            deger.append("-2") 
        elif i == 13:
           deger.append("-1") 
        elif i == 37 :
            deger.append("0")
        elif i == 57:
            deger.append("-3")
        elif i == 64 :
            deger.append("-4")
            deger.append("-3")
        elif (i-25) % 15 == 0 and i >24  and i < 66 :
            deger.append("-1")
            deger.append("-4")  
        elif i == 67:
            deger.append("-1")
            deger.append("-4")
            deger.append("-4")
            deger.append("-4")
        elif i == 76:
            deger.append("-4")
        elif i == 78:
            deger.append("-1")
            deger.append("-4")
        elif i == 89:
           deger.append("-1") 
        elif i == 101:
           deger.append("-1")  
        elif i == 115:
           deger.append("-1")  
        elif i == 128:
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