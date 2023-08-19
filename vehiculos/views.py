from django.shortcuts import render

def vehiculos(request):
    context={

    }
    return render(request,'vehiculos/vehiculos.html',context)

def vehiculos_crear(request):
    context={

    }
    return render(request,'vehiculos/vehiculos-crear.html',context)
