from django.urls import path

from jucator import views

urlpatterns = [

    path('creaza-jucator/', views.JucatorCreateView.as_view(), name="creaza_jucator"),
    path('lista-cu-jucatori/', views.JucatorListView.as_view(), name="lista_cu_jucatori"),
]