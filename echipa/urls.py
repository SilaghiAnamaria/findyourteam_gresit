from django.urls import path

from echipa import views

urlpatterns = [

    path('creaza-echipa/', views.EchipaCreateView.as_view(), name="creaza_echipa"),
    path('lista-cu-echipe/', views.EchipaListView.as_view(), name="lista_cu_echipe"),
]