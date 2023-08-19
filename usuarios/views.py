from django.shortcuts import render


def usuarios(request):
    context={

    }
    return render(request,'usuarios/usuarios.html',context)

def usuarios_crear(request):
    context={

    }
    return render(request,'usuarios/usuarios-crear.html',context)