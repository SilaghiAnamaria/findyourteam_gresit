from django.db import models


class Locatie(models.Model):

    denumire = models.CharField(max_length=60)
    localitate = models.CharField(max_length=20)
    adresa = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    deschisa = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.denumire} {self.localitate}"
