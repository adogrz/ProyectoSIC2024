from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import JsonResponse
from .models import PuestoTrabajo


def lista_puestos(request):
    puestos = PuestoTrabajo.objects.all().order_by('nombre')
    return render(request, 'lista_puestos.html', {'puestos': puestos})


def agregar_puesto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        sueldo_mensual = request.POST.get('sueldo_mensual')
        sueldo_hora = request.POST.get('sueldo_hora')
        es_administrativo = request.POST.get('es_administrativo')

        PuestoTrabajo.objects.create(
            nombre=nombre,
            sueldo_mensual=sueldo_mensual,
            sueldo_por_hora=sueldo_hora,
            es_administrativo=es_administrativo
        )
        return redirect('lista_puestos')
    return render(request, 'agregar_puesto.html')


def calcular_costo_mano_obra(request):
    puestos = PuestoTrabajo.objects.filter(es_administrativo=False).order_by('nombre')
    return render(
        request,
        'calcular_mano_obra.html',
        {'puestos': puestos}
    )


def obtener_sueldo_por_hora(request, puesto_id):
    puesto = PuestoTrabajo.objects.get(id=puesto_id)
    return JsonResponse({'sueldo_por_hora': puesto.sueldo_por_hora})


def calcular_costos_indirectos(request):
    # Obtener la suma de los sueldos mensuales del personal administrativo
    gasto_administrativo = PuestoTrabajo.objects.filter(es_administrativo=True).aggregate(
        total_gasto_administrativo=Sum('sueldo_mensual')
    )['total_gasto_administrativo'] or 0  # Valor por defecto en caso de que no haya registros administrativos

    return render(request, 'calcular_costos_indirectos.html', {
        'gasto_administrativo': gasto_administrativo
    })
