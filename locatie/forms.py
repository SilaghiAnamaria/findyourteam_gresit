from django import forms
from django.forms import TextInput, Select, Textarea

from locatie.models import Locatie


class LocatieForm(forms.ModelForm):
    class Meta:
        model = Locatie
        fields = [ "denumire","localitate", "adresa", "description", ]
        widgets = {
            "denumire": TextInput(attrs={'placeholder': "Introduceti numele locatiei", "class": "form-control"}),
            "localitate": TextInput(attrs={'placeholder': "Introduceti localitatea", "class": "form-control"}),
            "adresa": TextInput(attrs={'placeholder': "Introduceti adresa", "class": "form-control"}),
            "description": Textarea(attrs={"placeholder": "Faceti o descriere a locatiei", "class": "form-control"}),

        }