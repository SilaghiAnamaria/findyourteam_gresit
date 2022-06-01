from django import forms
from django.forms import TextInput, Select, Textarea

from jucator.models import Jucator


class JucatorForm(forms.ModelForm):
    class Meta:
        model = Jucator
        fields = "__all__"
        widgets = {
            "prenume": TextInput(attrs={'placeholder': "Introduceti prenumele", "class": "form-control"}),
            "nume": Textarea(attrs={'placeholder': "Introduceti numele", "class": "form-control"}),
            "porecla": TextInput(attrs={'placeholder': "Introduceti o porecla (optional)", "class": "form-control"}),
            "varsta": TextInput(attrs={'placeholder': "Introduceti varsta", "class": "form-control"}),
            "localitate": TextInput(attrs={'placeholder': "Introduceti localitatea", "class": "form-control"}),
            "gen": Select(attrs={"class": "form-select"}),
            "descriere": Textarea(attrs={"placeholder":"Faceti-va o descriere", "class" : "form-control"}),

        }