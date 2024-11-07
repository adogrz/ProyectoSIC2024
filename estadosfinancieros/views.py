from django.shortcuts import render
from libromayor.models import CatalogoCuenta

def balance_general(request):
    # Obtener todas las cuentas de tipo Activo y Pasivo, y la cuenta con nombre "Capital Social"
    catalogo_cuentas = CatalogoCuenta.objects.filter(tipoDeCuenta__in=["Activo", "Pasivo"])

    total_debe = 0
    total_haber = 0

    # Calcular el total de debe y haber solo para las cuentas seleccionadas
    for cuenta in catalogo_cuentas:
        # Asegúrate de que los valores de 'debe' y 'haber' no sean nulos
        cuenta.debe = cuenta.debe if cuenta.debe is not None else 0
        cuenta.haber = cuenta.haber if cuenta.haber is not None else 0

        # Sumar los valores a los totales
        total_debe += cuenta.debe
        total_haber += cuenta.haber

    context = {
        'catalogo_cuentas': catalogo_cuentas,  # Pasar las cuentas filtradas al contexto
        'total_debe': total_debe,
        'total_haber': total_haber,
    }

    return render(request, 'Balance_general.html', context)
