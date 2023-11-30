from django.db import models

# Create your models here.


class Dosen(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.nama}"


class Profil(models.Model):
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    fb = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.dosen}"
