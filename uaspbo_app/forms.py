from django.forms import ModelForm
from django import forms
from .models import *

class FormGaram(ModelForm):
    class Meta:
        model = Garam
        fields = '__all__'

        widgets = {
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'Koordinat', 'required':'required'}),
            'provinsi' : forms.TextInput({'class':'form-control', 'placeholder':'Provinsi', 'required':'required'}),
            'tahun_2017' : forms.NumberInput({'class':'form-control', 'placeholder':'Jumlah (Ton)'}),
            'tahun_2018' : forms.NumberInput({'class':'form-control', 'placeholder':'Jumlah (Ton)'}),
            'tahun_2019' : forms.NumberInput({'class':'form-control', 'placeholder':'Jumlah (Ton)'}),
            'tahun_2020' : forms.NumberInput({'class':'form-control', 'placeholder':'Jumlah (Ton)'}),   
            'jenis_id' : forms.Select({'class':'form-control', 'placeholder':'Jenis Usaha', 'required':'required'}),
        }


class FormBerita(ModelForm):
    class Meta:
        model = Berita
        fields = '__all__'

        widgets = {
            'publikasi' : forms.DateInput({'type':'date','class':'form-control', 'placeholder':'Publikasi', 'required':'required'}),
            'judul' : forms.TextInput({'class':'form-control', 'placeholder':'Judul', 'required':'required'}),
            'isi' : forms.TextInput({'class':'form-control', 'placeholder':'Isi', 'required':'required'}),
            'link' : forms.TextInput({'class':'form-control', 'placeholder':'Link', 'required':'required'}),
            'img' : forms.TextInput({'class':'form-control', 'placeholder':'Gambar (Ketentuan: Pilih salt1.jpg-salt ke-n.jpg)', 'required':'required'}),    
            'macam_id' : forms.Select({'class':'form-control', 'placeholder':'Macam Berita', 'required':'required'}),
        }
