from django.shortcuts import render,redirect, get_object_or_404
from productos.models import Producto
from productos.forms import ProductoForm, ProductoUpdateForm
from django.contrib import messages
from django.urls import reverse, resolve
from django.urls import reverse
from . import urls
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def producto_crear(request):
    titulo="Producto"
    if request.method== 'POST':
        form=ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            producto = form.save()

            messages.success(request,'Se ha creado correctamente el producto')
            return redirect('productos')
        else: 
            messages.error(request, 'Por favor rectifique los datos del producto')
    else:
        form= ProductoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"productos/productos/crear.html", context)

@login_required
def producto_listar(request, visualizar=1):
    titulo="Producto"
    modulo="Productos"

    if visualizar==1:
        productos=Producto.objects.filter(estado=visualizar)
    else:
        productos=Producto.objects.all()

    paginator = Paginator(productos,5) #5 productos por página
    page_number = request.GET.get('page') #número de pagina
    try:
        productos = paginator.page(page_number)
    except PageNotAnInteger:
        # es para que en caso de que el número de pagina no sea entero, mostrar la primera página
        productos = paginator.page(1)
    except EmpyPage:
        # en caso de que el número de pagina este fuera de rango se muestra la ultima pagina
        productos = paginator.page(paginator.num_pages)
    context={
        "titulo":titulo,
        "modulo":modulo,
        "productos":productos,
        "visualizar":visualizar
    }
    return render(request, "productos/productos/listar.html", context)
@login_required
def producto_modificar(request,pk):
    titulo="Producto"
    producto= Producto.objects.get(id=pk)

 
 
    if request.method == 'POST':
        form=ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente el formulario')
            return redirect ('productos')
    else:
        form= ProductoUpdateForm(instance=producto)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"productos/productos/modificar.html", context)

def producto_eliminar(request,pk):
    producto=Producto.objects.filter(id=pk)
    producto.update(
        estado="0"
    )
    return redirect ('productos')


