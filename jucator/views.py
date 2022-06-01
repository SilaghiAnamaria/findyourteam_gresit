
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from jucator.models import Jucator


class JucatorCreateView(CreateView):
    template_name = "jucator/creaza_jucator.html"
    model = Jucator
    success_url = reverse_lazy("lista_cu_jucatori")  # unde se duce dupa ce dam submit
    # permission_required = 'jucator.add_jucator'


class JucatorListView(ListView):
    template_name = "jucator/lista_cu_jucatori.html"
    model = Jucator
    context_object_name = "toti_jucatorii"
    # permission_required = 'jucator.add_jucator'
