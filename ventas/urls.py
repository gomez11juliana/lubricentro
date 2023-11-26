from django.urls import path
from ventas.views import venta_listar, venta_crear, venta_modificar, venta_eliminar

urlpatterns =[
path('venta/<int:visualizar>/', venta_listar, name="ventas"),
path('venta/', venta_listar, name="ventas"),

path('venta/crear/', venta_crear, name="venta-crear"),
path('venta/modificar/<int:pk>/', venta_modificar, name="ventas-modificar"),
path('venta/eliminar/<int:pk>/', venta_eliminar, name="ventas-eliminar"),


]