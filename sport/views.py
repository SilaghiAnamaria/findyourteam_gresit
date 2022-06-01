from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from sport.models import Sport


class SportCreateView(CreateView):
    template_name = "sport/creaza_sport.html"
    model = Sport
    success_url = reverse_lazy("lista_de_sporturi")  # unde se duce dupa ce dam submit
    # permission_required = 'sport.add_sport'


class SportListView(ListView):
    template_name = 'sport/lista_cu_sporturi.html'
    model = Sport
    context_object_name = "toate_sporturile"


