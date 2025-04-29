from django.shortcuts import render, redirect
from .models import ContratoPlan
from django.contrib import messages
from datetime import timedelta
from dateutil.relativedelta import relativedelta  # Para sumar meses
from django.db.models import Sum, Count
from .models import Curso
from collections import defaultdict
from unidecode import unidecode
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models.functions import TruncMonth

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


def index(request):
    cursos = Curso.objects.all()

    dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    dias_clave = [unidecode(dia).lower() for dia in dias_semana]  # sin tildes

    horario = defaultdict(lambda: {k: [] for k in dias_clave})
    horas_set = set()

    for curso in cursos:
        hora = curso.hora.strftime('%H:%M')
        dia = unidecode(curso.dia.strip()).lower()  # <- quitar tildes y espacios
        horas_set.add(hora)
        if dia in horario[hora]:
            horario[hora][dia].append(curso)

    horas_ordenadas = sorted(horas_set)

    return render(request, 'index.html', {
        'horario': horario,
        'dias_semana': dias_semana,  # con tildes para mostrar
        'horas_disponibles': horas_ordenadas
    })

def panel_admin(request):
    total_contratos = ContratoPlan.objects.count()
    total_monto = ContratoPlan.objects.aggregate(Sum('precio'))['precio__sum'] or 0
    cursos = Curso.objects.all()

    # Nuevo: resumen de contratos por mes
    contratos_por_mes = (
        ContratoPlan.objects
        .annotate(mes=TruncMonth('fecha_contratacion'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )

    return render(request, 'panel_admin.html', {
        'total_contratos': total_contratos,
        'total_monto': total_monto,
        'cursos': cursos,
        'contratos_por_mes': contratos_por_mes
    })

def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('panel_admin')

def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        curso.nombre = request.POST.get('nombre')
        curso.profesor = request.POST.get('profesor')
        curso.dia = request.POST.get('dia')
        curso.hora = request.POST.get('hora')
        curso.duracion_minutos = request.POST.get('duracion_minutos')
        curso.save()
        return redirect('panel_admin')

    return render(request, 'editar_curso.html', {'curso': curso})