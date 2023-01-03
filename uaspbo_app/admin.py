from django.contrib import admin

# Register your models here.
from .models import *

class garamadmin(admin.ModelAdmin):
    list_display = ['koordinat', 'provinsi', 'tahun_2017', 'tahun_2018', 'tahun_2019', 'tahun_2020']
    search_fields = ['koordinat', 'provinsi']
    list_filter = ['jenis_id']
    list_per_page = 5

admin.site.register(Garam, garamadmin)
admin.site.register(Jenis)


class beritaadmin(admin.ModelAdmin):
    list_display = ['publikasi', 'judul', 'isi', 'link', 'img']
    search_fields = ['judul', 'publikasi']
    list_filter = ['macam_id']
    list_per_page = 5

admin.site.register(Berita, beritaadmin)
admin.site.register(Macam)