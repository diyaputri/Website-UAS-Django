"""uaspbo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from uaspbo_app.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('berita/', berita, name='berita'),
    path('garamuser/', garamuser, name='garamuser'),
    path('garamadmin/', garamadmin, name='garamadmin'),
    path('registrasi/', registrasi, name='registrasi'),
    path('tambahgaram/', tambahgaram),
    path('tambahberita/', tambahberita),
    path('garamadmin/ubahgaram/<int:mn>', ubahgaram, name='update'),
    path('garamadmin/deletegaram/<int:mn>', deletegaram, name='delete'),
    path('berita/ubahberita/<int:id>', ubahberita, name='update2'),
    path('berita/deleteberita/<int:id>', deleteberita, name='delete2'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

]
