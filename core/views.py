from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def contacto(request):
    return render(request, 'contacto.html')

def seleccionar_plan(request, plan_nombre, precio):
    return render(request, 'planes.html', {'plan': plan_nombre, 'precio': precio})

