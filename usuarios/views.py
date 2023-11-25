
from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm,UsuarioUpdateForm

from django.contrib import messages
from django.urls import reverse, resolve
from django.urls import reverse
from . import urls
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def usuario_crear(request):
    titulo="Usuario"
    
    if request.method== 'POST':
        form= UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            usuario = form.save()
  
            usuario.save()
            messages.success(request, 'El usuario se ha creado correctamente.')

            return redirect('usuarios')
        else:
            messages.error(request, 'Los datos del usuario tienen errores.')
    else:
        form= UsuarioForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/usuarios/crear.html", context)

@login_required
def usuario_listar(request, visualizar=1):
    titulo="Usuario"
    modulo="Usuarios"
    
    
    if visualizar==1:
        usuarios= Usuario.objects.filter(estado=visualizar)
    else:
        usuarios= Usuario.objects.all()

    paginator = Paginator(usuarios, 3) # 3 usuarios por página
    page_number = request.GET.get('page') # número de página actual
    try:
        usuarios = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la primera página.
        usuarios = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango, mostrar la última página.
        usuarios = paginator.page(paginator.num_pages)
    context={
       

        "titulo":titulo,
        "modulo":modulo,
        "usuarios":usuarios,
        "visualizar":visualizar
    }
    return render(request,"usuarios/usuarios/listar.html", context)

@login_required
def usuario_modificar(request,pk):
    titulo="Usuario"
    usuario= Usuario.objects.get(id=pk)
    
    if request.method== 'POST':
        form= UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('usuarios')
    else:
        form= UsuarioUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/usuarios/modificar.html", context)


def usuario_eliminar(request,pk):
    usuario= Usuario.objects.filter(id=pk)
    
    usuario.update(
        estado="0"
    )
    return redirect('usuarios')
   

