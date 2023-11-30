from django.contrib import admin
from .models import Dosen, Profil

# Register your models here.
admin.site.register(Dosen)


class ProfilAdmin(admin.ModelAdmin):
    list_display = ("dosen", "email", "fb",)


admin.site.register(Profil, ProfilAdmin)
