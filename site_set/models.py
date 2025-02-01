from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class sayfa_logosu(models.Model):
    sayfa_logo = models.FileField(upload_to='logo/',blank = True,null = True,verbose_name="Sayfaya Logo Ekleyin")
class sayfa_iconu(models.Model):
    sayfa_logo = models.FileField(upload_to='icon/',blank = True,null = True,verbose_name="Sayfaya icon Ekleyin")
class site_adi(models.Model):
    site_adi_genel = models.CharField(max_length=200)
    def __str__(self):
        return self.site_adi_genel
class numara(models.Model):
    sirket_numarasi = models.CharField(max_length=11)
    def __str__(self):
        return self.sirket_numarasi
class adres(models.Model):
    sirket_adresi = models.CharField(max_length=200)
    def __str__(self):
        return self.sirket_adresi
class email_adres(models.Model):
    sirket_email_adresi = models.EmailField(max_length=200)
    def __str__(self):
        return self.sirket_email_adresi
class sosyalmedyaTw(models.Model):
    link = models.CharField(max_length=400)
    def __str__(self):
        return self.link
class sosyalmedyafb(models.Model):
    link = models.CharField(max_length=400)
    def __str__(self):
        return self.link
class sosyalmedyaInsgr(models.Model):
    link = models.CharField(max_length=400)
    def __str__(self):
        return self.link
class banner(models.Model):
    sayfa_sirasi = models.BigIntegerField(null=True)
    baner_resim = models.FileField(upload_to='banner/',blank = True,verbose_name="Sayfaya resim Ekleyiniz")


class hakkimizda(models.Model):
    hakkimda = RichTextField()
class iletisim(models.Model):
    iletisim_yollari = RichTextField()

class resimler (models.Model):
    resim = models.FileField(upload_to='resimler/',blank = True,verbose_name="Sayfaya resim Ekleyiniz")

class aciklama(models.Model):
    footer_aciklama= models.TextField()
    def __str__(self):
        return self.footer_aciklama
