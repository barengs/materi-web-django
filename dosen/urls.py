from django.urls import path
from . import views

urlpatterns = [
    path('dosen', views.dosen, name='dosen'),
    path('dosen/<int:id>', views.detildosen, name='detildosen'),
    path('karyawan', views.karyawan, name='karyawan'),
]
