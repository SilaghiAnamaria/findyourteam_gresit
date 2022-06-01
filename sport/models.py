from django.db import models


class Sport(models.Model):

    denumire = models.CharField(max_length=60)
    localitate = models.CharField(max_length=30)
    descriere = models.TextField(max_length=1000)
    numar_min_jucatori = models.IntegerField(2)
    numar_max_jucatori = models.IntegerField(3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.denumire} {self.localitate}"

