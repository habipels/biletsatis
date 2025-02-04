from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class etkinlikler(models.Model):
    etkinlik_adi = models.CharField(max_length=200)
    etkinlik_aciklama = models.TextField()
    etkinlik_tarihi = models.DateTimeField()
    etkinlik_resim = models.FileField(upload_to='etkinlikler/',blank = True,verbose_name="Etkinlik Resmi")
    etkinlik_yeri = models.CharField(max_length=200)
    etkinlik_linki = models.CharField(max_length=200)
    etkinlik_organizator = models.CharField(max_length=200)
    etkinlik_fiyati = models.FloatField(default=0)
    etkinlik_katitim_sayisi = models.IntegerField(default=0)
    etkinlik_bilgilendirmesi = RichTextField()
    def __str__(self):
        return self.etkinlik_adi