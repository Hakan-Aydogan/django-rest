from django.db import models

# Create your models here.


class Makale(models.Model):
    yazar = models.CharField(max_length=150)
    baslik = models.CharField(max_length=150)
    aciklama = models.CharField(max_length=250)
    metin = models.TextField()
    aktif = models.BooleanField(default=True)
    yayinlanma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik
