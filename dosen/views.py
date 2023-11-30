from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dosen, Profil
# Create your views here.


def dosen(request):
    data = Dosen.objects.all()  # ambil semua data dari table dosen
    template = loader.get_template('dosen.html')
    context = {
        "contoh": 'ini data dari variable',
        "dosen": data,
    }
    return HttpResponse(template.render(context, request))


def detildosen(request, id):
    data = Dosen.objects.filter(id=id).first()
    context = {
        'data_dosen': data
    }
    template = loader.get_template('detil_dosen.html')
    return HttpResponse(template.render(context))


def karyawan(request):
    template = loader.get_template('karyawan.html')
    return HttpResponse(template.render())
