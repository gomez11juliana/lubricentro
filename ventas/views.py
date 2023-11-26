from django.shortcuts import render,redirect, get_object_or_404
from ventas.models import Venta
from ventas.forms import VentaForm, VentaUpdateForm
from django.contrib import messages
from django.urls import reverse, resolve
from django.urls import reverse
from . import urls
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def venta_crear(request):
    titulo="Venta"
    if request.method== 'POST':
        form=VentaForm(request.POST,request.FILES)
        if form.is_valid():
            venta = form.save()

            messages.success(request,'Se ha creado correctamente la venta')
            return redirect('ventas')
        else: 
            messages.error(request, 'Por favor rectifique los datos de la venta')
    else:
        form= VentaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"ventas/ventas/crear.html", context)

@login_required
def venta_listar(request, visualizar=1):
    titulo="Venta"
    modulo="Ventas"

    if visualizar==1:
        ventas=Venta.objects.filter(estado=visualizar)
    else:
        ventas=Venta.objects.all()

    paginator = Paginator(ventas,5) #5 ventas por página
    page_number = request.GET.get('page') #número de pagina
    try:
        ventas = paginator.page(page_number)
    except PageNotAnInteger:
        # es para que en caso de que el número de pagina no sea entero, mostrar la primera página
        ventas = paginator.page(1)
    except EmpyPage:
        # en caso de que el número de pagina este fuera de rango se muestra la ultima pagina
        ventas = paginator.page(paginator.num_pages)
    context={
        "titulo":titulo,
        "modulo":modulo,
        "ventas":ventas,
        "visualizar":visualizar
    }
    return render(request, "ventas/ventas/listar.html", context)
@login_required
def venta_modificar(request,pk):
    titulo="Venta"
    venta= Venta.objects.get(id=pk)

 
 
    if request.method == 'POST':
        form=VentaUpdateForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente el formulario')
            return redirect ('ventas')
    else:
        form= VentaUpdateForm(instance=venta)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"ventas/ventas/modificar.html", context)

def venta_eliminar(request,pk):
    venta=Venta.objects.filter(id=pk)
    venta.update(
        estado="0"
    )
    return redirect ('ventas')


