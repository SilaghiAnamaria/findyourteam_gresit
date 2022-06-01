
from django.urls import reverse_lazy
from django.views.generic import CreateView

from echipa.forms import EchipaForm
from echipa.models import Echipa


class EchipaCreateView(CreateView):
    template_name = "echipa/creaza_echipa.html"
    model = Echipa
    form_class = EchipaForm
    success_url = reverse_lazy("lista_cu_echipe")  # unde se duce dupa ce dam submit
    # permission_required = 'echipa.add_echipa'


class EchipaListView(CreateView):
    template_name = "echipa/lista_cu_echipe.html"
    model = Echipa
    context_object_name = "toate_echipele"
    # permission_required = 'echipa.add_echipa'