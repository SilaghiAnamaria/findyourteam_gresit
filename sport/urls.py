from django.urls import path

from sport import views

urlpatterns = [

    path('creaza-sport/', views.SportCreateView.as_view(), name="creaza_sport"),
    path('lista-cu-sporturi/', views.SportListView.as_view(), name="lista_cu_sporturi"),
]