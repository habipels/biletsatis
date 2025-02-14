from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

class etkinlikler(models.Model):
    etkinlik_adi = models.CharField(max_length=200)
    etkinlik_aciklama = models.TextField()
    etkinlik_tarihi = models.DateTimeField()
    etkinlik_resim = models.FileField(upload_to='etkinlikler/', blank=True, verbose_name="Etkinlik Resmi")
    etkinlik_yeri = models.CharField(max_length=200)
    etkinlik_linki = models.CharField(max_length=200)
    etkinlik_organizator = models.CharField(max_length=200)
    etkinlik_fiyati = models.FloatField(default=0)
    etkinlik_katitim_sayisi = models.IntegerField(default=0)
    etkinlik_bilgilendirmesi = HTMLField(blank=True, default="")
    koltuk_duzeni_var_mi = models.BooleanField(default=False)
    def __str__(self):
        return self.etkinlik_adi

class etkinlik_sepeti(models.Model):
    etkinlik = models.ForeignKey(etkinlikler, on_delete=models.CASCADE)
    katilimci = models.CharField(max_length=200)
    katilimci_email = models.EmailField()
    katilimci_telefon = models.CharField(max_length=200)
    satin_alama_durumu = models.BooleanField(default=False)
    satin_alma_tarihi = models.DateTimeField(blank=True, null=True)
    toplam_fiyat = models.FloatField(default=0)
    elden_satis = models.BooleanField(default=False)
    elden_satis_yapilan_ip = models.GenericIPAddressField(blank=True, null=True)
    def __str__(self):
        return f"{self.katilimci} - {self.etkinlik.etkinlik_adi}"

class sepet_koltuk(models.Model):
    etkinlik_sepeti = models.ForeignKey(etkinlik_sepeti, on_delete=models.CASCADE)
    koltuk_no = models.IntegerField()
    def __str__(self):
        return  f"{self.etkinlik_sepeti.katilimci} - Koltuk No: {self.koltuk_no}"

class etkinlik_yorumlari(models.Model):
    etkinlik = models.ForeignKey(etkinlikler, on_delete=models.CASCADE)
    yorum_yapan = models.CharField(max_length=200)
    yorum = models.TextField()
    yorum_tarihi = models.DateTimeField()
    yorum_yapan_ip = models.GenericIPAddressField()
    yorum_yapan_resmi = models.FileField(upload_to='yorumlar/', blank=True, verbose_name="Yorum Yapan Resmi")
    etkinlik_puan = models.IntegerField()
    def __str__(self):
        return self.yorum_yapan

class etkinlik_bildirimi(models.Model):
    etkinlik = models.ForeignKey(etkinlikler, on_delete=models.CASCADE, null=True, blank=True)
    bildirim_tarihi = models.DateTimeField()
    bildirim_mesaji = models.TextField()
    etkinlik_url = models.CharField(max_length=200)
    def __str__(self):
        return self.bildirim_mesaji

class etkinlik_koltuk_fiyaatlari(models.Model):
    etkinlik = models.ForeignKey(etkinlikler, on_delete=models.CASCADE)
    koltuk_no = models.IntegerField()
    fiyat = models.FloatField()
    def __str__(self):
        return str(self.koltuk_no)

    class Meta:
        app_label = 'etkinlikler'
