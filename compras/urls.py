from django.urls import path
from compras.views import compra_listar, compra_crear, compra_modificar, compra_eliminar

urlpatterns =[
path('compra/<int:visualizar>/', compra_listar, name="compras"),
path('compra/', compra_listar, name="compras"),

path('compra/crear/', compra_crear, name="compras-crear"),
path('compra/modificar/<int:pk>/', compra_modificar, name="compras-modificar"),
path('compra/eliminar/<int:pk>/', compra_eliminar, name="compras-eliminar"),


]