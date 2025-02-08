from django.contrib import admin
from .models import *

class EtkinliklerAdmin(admin.ModelAdmin):
    list_display = ('etkinlik_adi', 'etkinlik_tarihi', 'etkinlik_yeri', 'etkinlik_organizator', 'etkinlik_fiyati')
    search_fields = ('etkinlik_adi', 'etkinlik_yeri', 'etkinlik_organizator')
    list_filter = ('etkinlik_tarihi', 'etkinlik_yeri', 'etkinlik_organizator')

class EtkinlikSepetiAdmin(admin.ModelAdmin):
    list_display = ('etkinlik', 'katilimci', 'katilimci_email', 'katilimci_telefon', 'satin_alama_durumu', 'toplam_fiyat', 'satin_alma_tarihi')
    search_fields = ('katilimci', 'katilimci_email', 'katilimci_telefon')
    list_filter = ('satin_alama_durumu', 'satin_alma_tarihi', 'etkinlik')

class SepetKoltukAdmin(admin.ModelAdmin):
    list_display = ('etkinlik_sepeti', 'koltuk_no')
    search_fields = ('etkinlik_sepeti__katilimci', 'koltuk_no')
    list_filter = ('etkinlik_sepeti__etkinlik',)

admin.site.register(etkinlikler, EtkinliklerAdmin)
admin.site.register(etkinlik_sepeti, EtkinlikSepetiAdmin)
admin.site.register(sepet_koltuk, SepetKoltukAdmin)
admin.site.register(etkinlik_yorumlari)
admin.site.register(etkinlik_bildirimi)
admin.site.register(etkinlik_koltuk_fiyaatlari)