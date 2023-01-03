from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def registrasi(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin Berhasil Dibuat!")
            return redirect('registrasi')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('registrasi')
    else:
        form = UserCreationForm()
        data = {
            'form':form,
        }
    return render(request, 'registrasi.html', data)

def index(request):
    artikel = Berita.objects.all()
    data = {
        'Title' : "Home - Salt",
        'artikel' : artikel,
    }
    return render(request, 'index.html', data)


@login_required(login_url=settings.LOGIN_URL)
def berita(request):
    artikel = Berita.objects.all()
    data = {
        'Title' : "Kelola Berita - Salt Admin",
        'artikel' : artikel,
    }
    return render(request, 'berita.html', data)


def garamuser(request):
    produksi = Garam.objects.all()
    data = {
        'Title' : "Produksi Garam - Salt",
        'produksi' : produksi,
    }
    return render(request, 'garamuser.html', data)

@login_required(login_url=settings.LOGIN_URL)
def garamadmin(request):
    produksi = Garam.objects.all()
    data = {
        'Title' : "Kelola Garam - Salt Admin",
        'produksi' : produksi,
    }
    return render(request, 'garamadmin.html', data)


@login_required(login_url=settings.LOGIN_URL)
def tambahberita(request):
    if request.POST:
        form = FormBerita(request.POST)
        if form.is_valid():
            form.save()
            form = FormBerita()
            artikel = Berita.objects.all()
            pesan = "Data Berita Berhasil Ditambahkan!"
            data = {
            'Title' : "Kelola Berita - Salt Admin",
            'artikel' : artikel,
            'form'  : form,
            'pesan' : pesan,
            }
            return render(request, 'tambahberita.html', data)
    else:
        form = FormBerita()
        artikel = Berita.objects.all()
        data = {
           'Title' : "Kelola Berita - Salt Admin",
           'artikel' : artikel,
           'form'  : form,
        }
    return render(request, 'tambahberita.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambahgaram(request):
    if request.POST:
        form = FormGaram(request.POST)
        if form.is_valid():
            form.save()
            form = FormGaram()
            produksi = Garam.objects.all()
            pesan = "Data Produksi Garam Berhasil Ditambahkan!"
            data = {
            'Title' : "Kelola Garam - Salt Admin",
            'produksi' : produksi,
            'form'  : form,
            'pesan' : pesan,
            }
            return render(request, 'tambahgaram.html', data)
    else:
        form = FormGaram()
        produksi = Garam.objects.all()
        data = {
           'Title' : "Kelola Garam - Salt Admin",
           'produksi' : produksi,
           'form'  : form,
        }
    return render(request, 'tambahgaram.html', data)


@login_required(login_url=settings.LOGIN_URL)
def ubahberita(request, id):
    ubahartikel = Berita.objects.get(pk=id)
    if request.POST:
        form = FormBerita(request.POST, instance=ubahartikel)
        if form.is_valid():
            form.save()
            pesan = "Berita Berhasil Diubah!"
            data = {
                'Title' : "Kelola Berita - Salt Admin",
                'berita' : ubahartikel,
                'form'  : form,
                'pesan' : pesan,
            }
            return render(request, 'ubahberita.html', data)
    else:
        form = FormBerita(instance=ubahartikel)
        data = {
        'Title' : "Kelola Berita - Salt Admin",
        'berita' : ubahartikel,
        'form'  : form,
        }
    return render(request, 'ubahberita.html', data)

@login_required(login_url=settings.LOGIN_URL) 
def deleteberita(request, id):
    berita = Berita.objects.get(pk=id)
    berita.delete()
    
    return redirect("/berita/")

@login_required(login_url=settings.LOGIN_URL)
def ubahgaram(request, mn):
    ubahproduksi = Garam.objects.get(pk=mn)
    if request.POST:
        form = FormGaram(request.POST, instance=ubahproduksi)
        if form.is_valid():
            form.save()
            pesan = "Produksi Garam Berhasil Diubah!"
            data = {
                'Title' : "Kelola Garam - Salt Admin",
                'garam' : ubahproduksi,
                'form'  : form,
                'pesan' : pesan,
            }
            return render(request, 'ubahgaram.html', data)
    else:
        form = FormGaram(instance=ubahproduksi)
        data = {
        'Title' : "Kelola Garam - Salt Admin",
        'garam' : ubahproduksi,
        'form'  : form,
         }
    return render(request, 'ubahgaram.html', data)

@login_required(login_url=settings.LOGIN_URL) 
def deletegaram(request, mn):
    garam = Garam.objects.get(pk=mn)
    garam.delete()
    
    return redirect("/garamadmin/")
