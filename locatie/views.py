
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from locatie.forms import LocatieForm
from locatie.models import Locatie


class LocatieCreateView(CreateView):
    template_name = "locatie/creaza_locatie.html"
    model = Locatie
    form_class = LocatieForm
    success_url = reverse_lazy("lista_locatii")  # unde se duce dupa ce dam submit
    # permission_required = 'locatie.add_locatie'



class LocatieListView(ListView):
    template_name = "locatie/lista_cu_locatii.html"
    model = Locatie
    context_object_name = "toate_locatiile"
    # permission_required = 'locatie.add_locatie'
