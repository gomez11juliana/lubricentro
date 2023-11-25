from django.urls import path
from productos.views import producto_listar, producto_crear, producto_modificar, producto_eliminar

urlpatterns =[
path('producto/<int:visualizar>/', producto_listar, name="productos"),
path('producto/', producto_listar, name="productos"),

path('producto/crear/', producto_crear, name="productos-crear"),
path('producto/modificar/<int:pk>/', producto_modificar, name="productos-modificar"),
path('producto/eliminar/<int:pk>/', producto_eliminar, name="productos-eliminar"),


]