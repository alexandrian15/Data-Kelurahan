from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_lengkap