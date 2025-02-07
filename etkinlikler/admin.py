from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(etkinlikler)
admin.site.register(etkinlik_sepeti)
admin.site.register(sepet_koltuk)
admin.site.register(etkinlik_yorumlari)
admin.site.register(etkinlik_bildirimi)
admin.site.register(etkinlik_koltuk_fiyaatlari)
# Compare this snippet from etkinlikler/views.py: