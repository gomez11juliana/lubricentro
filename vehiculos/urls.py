from django.urls import path
from vehiculos.views import vehiculos


urlpatterns = [
    path('',vehiculos,name="vehiculos"),
]