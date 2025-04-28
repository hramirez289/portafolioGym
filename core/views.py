from django.shortcuts import render, redirect
from .models import ContratoPlan
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def contacto(request):
    return render(request, 'contacto.html')

def seleccionar_plan(request, plan_nombre, precio):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        sexo = request.POST.get('sexo')
        telefono = request.POST.get('telefono')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        metodo_pago = request.POST.get('metodo_pago')

        ContratoPlan.objects.create(
            plan=plan_nombre,
            precio=precio,
            rut=rut,
            nombre_completo=nombre,
            email=email,
            sexo=sexo,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            metodo_pago=metodo_pago
        )

        messages.success(request, '¡Gracias por contratar tu plan!')
        return redirect('index')  # Redirige al inicio

    return render(request, 'planes.html', {'plan': plan_nombre, 'precio': precio})
