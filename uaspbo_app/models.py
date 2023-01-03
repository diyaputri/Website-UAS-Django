from django.db import models

# Create your models here.

class Jenis(models.Model):
   nama = models.CharField(max_length=40)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Garam(models.Model):
   koordinat = models.CharField(max_length=100)
   provinsi = models.CharField(max_length=60)
   tahun_2017 = models.IntegerField(null=True)
   tahun_2018 = models.IntegerField(null=True)
   tahun_2019 = models.IntegerField(null=True)
   tahun_2020 = models.IntegerField(null=True)
   jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.provinsi


class Macam(models.Model):
   nama = models.CharField(max_length=40)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Berita(models.Model):
   publikasi = models.DateField(null=True)
   judul = models.CharField(max_length=100)
   isi = models.TextField()
   link = models.CharField(max_length=100)
   img = models.CharField(null=True, max_length=40)
   macam_id = models.ForeignKey(Macam, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.judul