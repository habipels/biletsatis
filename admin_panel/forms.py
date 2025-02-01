from django import forms
from site_set.models import (
    sayfa_logosu, sayfa_iconu, site_adi, numara, adres, email_adres, 
    sosyalmedyaTw, sosyalmedyafb, sosyalmedyaInsgr, banner, hakkimizda, 
    iletisim, resimler, aciklama
)

class SayfaLogosuForm(forms.ModelForm):
    class Meta:
        model = sayfa_logosu
        fields = '__all__'

class SayfaIconuForm(forms.ModelForm):
    class Meta:
        model = sayfa_iconu
        fields = '__all__'

class SiteAdiForm(forms.ModelForm):
    class Meta:
        model = site_adi
        fields = '__all__'

class NumaraForm(forms.ModelForm):
    class Meta:
        model = numara
        fields = '__all__'

class AdresForm(forms.ModelForm):
    class Meta:
        model = adres
        fields = '__all__'

class EmailAdresForm(forms.ModelForm):
    class Meta:
        model = email_adres
        fields = '__all__'

class SosyalMedyaTwForm(forms.ModelForm):
    class Meta:
        model = sosyalmedyaTw
        fields = '__all__'

class SosyalMedyaFbForm(forms.ModelForm):
    class Meta:
        model = sosyalmedyafb
        fields = '__all__'

class SosyalMedyaInsgrForm(forms.ModelForm):
    class Meta:
        model = sosyalmedyaInsgr
        fields = '__all__'

class BannerForm(forms.ModelForm):
    class Meta:
        model = banner
        fields = '__all__'

class HakkimizdaForm(forms.ModelForm):
    class Meta:
        model = hakkimizda
        fields = '__all__'

class IletisimForm(forms.ModelForm):
    class Meta:
        model = iletisim
        fields = '__all__'

class ResimlerForm(forms.ModelForm):
    class Meta:
        model = resimler
        fields = '__all__'

class AciklamaForm(forms.ModelForm):
    class Meta:
        model = aciklama
        fields = '__all__'
