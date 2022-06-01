from django.urls import path

from userextend import views

urlpatterns = [

    path('creaza-user/', views.UserExtendCreateView.as_view(), name='creaza_user')
]