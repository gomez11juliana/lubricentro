from django.shortcuts import render

def servicios(request):
    context={

    }
    return render(request,'servicios/servicios.html',context)

def servicios_crear(request):
    context={

    }
    return render(request,'servicios/servicios-crear.html',context)