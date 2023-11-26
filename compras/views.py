from django.shortcuts import render,redirect, get_object_or_404
from compras.models import Compra
from compras.forms import CompraForm, CompraUpdateForm
from django.contrib import messages
from django.urls import reverse, resolve
from django.urls import reverse
from . import urls
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def compra_crear(request):
    titulo="Compra"
    if request.method== 'POST':
        form=CompraForm(request.POST,request.FILES)
        if form.is_valid():
            compra = form.save()

            messages.success(request,'Se ha creado correctamente la compra')
            return redirect('compras')
        else: 
            messages.error(request, 'Por favor rectifique los datos de la compra')
    else:
        form= CompraForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"compras/compras/crear.html", context)

@login_required
def compra_listar(request, visualizar=1):
    titulo="Compra"
    modulo="Compras"

    if visualizar==1:
        Compras=Compra.objects.filter(estado=visualizar)
    else:
        compras=Compra.objects.all()

    paginator = Paginator(compras,5) #5 compras por página
    page_number = request.GET.get('page') #número de pagina
    try:
        compras = paginator.page(page_number)
    except PageNotAnInteger:
        # es para que en caso de que el número de pagina no sea entero, mostrar la primera página
        compras = paginator.page(1)
    except EmpyPage:
        # en caso de que el número de pagina este fuera de rango se muestra la ultima pagina
        compras = paginator.page(paginator.num_pages)
    context={
        "titulo":titulo,
        "modulo":modulo,
        "compras":compras,
        "visualizar":visualizar
    }
    return render(request, "compras/compras/listar.html", context)
@login_required
def compra_modificar(request,pk):
    titulo="Compra"
    compra= Compra.objects.get(id=pk)

 
 
    if request.method == 'POST':
        form=CompraUpdateForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente el formulario')
            return redirect ('compras')
    else:
        form= CompraUpdateForm(instance=compra)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"compras/compras/modificar.html", context)

def compra_eliminar(request,pk):
    compra=Compra.objects.filter(id=pk)
    compra.update(
        estado="0"
    )
    return redirect ('compras')


