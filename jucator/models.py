from django.db import models



class Jucator(models.Model):
    gen_choices = (("barbat", "Barbat"), ("femeie", "Femeie"))

    prenume = models.CharField(max_length=20)
    nume = models.CharField(max_length=20)
    porecla = models.CharField(max_length=20)
    varsta = models.IntegerField()
    localitate = models.TextField(max_length=30)
    descriere = models.TextField(max_length=1000)
    gen = models.CharField(max_length=10, choices=gen_choices)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenume} {self.nume}"
