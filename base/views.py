from django.shortcuts import redirect, render
from usuarios.models import Usuario
from productos.models import Producto
from ventas.models import Venta
from compras.models import Compra
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required
def principal(request):
    titulo="Bienvenido al Sistema"
    usuarios= Usuario.objects.all().count()
    productos=Producto.objects.all().count()
    ventas=Venta.objects.all().count()
    compras=Compra.objects.all().count()
   
    

    context={
        
        "usuarios":usuarios,
        "productos":productos,
        "ventas":ventas,
        "compras":compras,
        "titulo":titulo,
        
    }
    return render(request, "index.html",context)

def logout_user(request):
    logout(request)
    return redirect('inicio')

