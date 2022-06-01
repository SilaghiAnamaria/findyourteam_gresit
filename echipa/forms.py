from django import forms
from django.forms import TextInput, Select, Textarea

from echipa.models import Echipa


class EchipaForm(forms.ModelForm):
    class Meta:
        model = Echipa
        fields = "__all__"
        widgets = {
            "nume": TextInput(attrs={'placeholder': "Introduceti numele echipei", "class": "form-control"}),
            "descriere": Textarea(attrs={'placeholder': "Introduceti o descriere a echipei", "class": "form-control"}),
            "numar_min_de_jucatori": TextInput(attrs={'placeholder': "Introduceti numarul minim de jucatori", "class": "form-control"}),
            "numar_max_de_jucatori": TextInput(attrs={'placeholder': "Introduceti numarul maxim de jucatori", "class": "form-control"}),
            "dificultate": Select(attrs={"class": "form-select"}),

        }