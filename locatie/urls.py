from django.urls import path

from locatie import views

urlpatterns = [

    path('creaza-locatie/', views.LocatieCreateView.as_view(), name="creaza_locatie"),
    path('lista-cu-locatii/', views.LocatieListView.as_view(), name='lista_cu_locatii'),

]