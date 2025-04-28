from django.shortcuts import render, redirect
from .models import ContratoPlan
from django.contrib import messages
from datetime import timedelta
from dateutil.relativedelta import relativedelta  # Para sumar meses
from django.db.models import Sum, Count

ADMIN_RUT = '99999999-9'

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


def mi_espacio(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        
        # 🚨 Validación para RUT de Administrador
        if rut == ADMIN_RUT:
            return redirect('panel_admin')

        try:
            contrato = ContratoPlan.objects.filter(rut=rut).latest('fecha_contratacion')
            fecha_inicio = contrato.fecha_contratacion
            fecha_termino = fecha_inicio + relativedelta(months=1)
            return render(request, 'mi_espacio.html', {
                'contrato': contrato,
                'fecha_inicio': fecha_inicio,
                'fecha_termino': fecha_termino
            })
        except ContratoPlan.DoesNotExist:
            return render(request, 'index.html', {'error': 'RUT no encontrado. Verifica e intenta nuevamente.'})

    return redirect('index')


def panel_admin(request):
    total_contratos = ContratoPlan.objects.count()
    total_monto = ContratoPlan.objects.aggregate(Sum('precio'))['precio__sum'] or 0

    return render(request, 'panel_admin.html', {
        'total_contratos': total_contratos,
        'total_monto': total_monto
    })