from django.urls import path
from inventario.views import inventario


urlpatterns = [
    path('',inventario,name="inventario"),
]