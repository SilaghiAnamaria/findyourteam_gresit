from django.db import models




class Echipa(models.Model):
    gen_choices = (("male", "Male"), ("female", "Female"))
    dificulty_choices = (("incepator", "Incepator"), ("intermediar", "Intermediar"), ("avanasat", "Avansat"))

    nume = models.CharField(max_length=20)
    numar_min_de_jucatori = models.IntegerField()
    numar_max_de_jucatori = models.IntegerField()
    descriere = models.TextField(max_length=1000)
    gen = models.CharField(max_length=10, choices=gen_choices)
    dificultate = models.CharField(max_length=20, choices=dificulty_choices)
    deschisa = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.gen} {self.dificultate}"