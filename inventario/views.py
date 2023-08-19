from django.shortcuts import render

def inventario(request):
    context={

    }
    return render(request,'inventario/inventario.html',context)

def inventario_crear(request):
    context={

    }
    return render (request, 'inventario/inventario-crear.html',context)