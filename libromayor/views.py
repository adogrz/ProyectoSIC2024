from django.shortcuts import render, redirect
from .models import CatalogoCuenta
from django.contrib import messages
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.contrib import messages
from libromayor.models import CatalogoCuenta

def transaccion(request):
    IVA_RATE = 0.13  # Tasa de IVA del 13%

    if request.method == 'POST':
        tipo_monto = request.POST.get('tipoDeMonto')  # Este debe coincidir con el nombre del campo en el modelo
        monto = request.POST.get('montoTransaccion')  # Este también debe coincidir
        codigo_cuenta = request.POST.get('codigo_cuenta')  # Obtener el código de la cuenta seleccionada

        # Validar que el código de la cuenta existe y obtener el objeto correspondiente
        try:
            registro_catalogo = CatalogoCuenta.objects.get(codigo=codigo_cuenta)

            # Calcular el IVA si la cuenta es "Debito Fiscal" o "Credito Fiscal"
            if registro_catalogo.codigo in ["1106.01", "2107.01"]:
                monto = float(monto) * IVA_RATE  # Solo el valor del IVA

            # Actualizar el monto en el debe o haber
            if tipo_monto == "Debe":
                nuevo_debe = (registro_catalogo.debe or 0) + float(monto)
                registro_catalogo.debe = nuevo_debe
            elif tipo_monto == "Haber":
                nuevo_haber = (registro_catalogo.haber or 0) + float(monto)
                registro_catalogo.haber = nuevo_haber

            registro_catalogo.save()  # Guardar los cambios en la cuenta

            messages.success(request, "Transacción agregada con éxito.")
            return redirect('formtransaccion')  # Redirige a la página deseada

        except CatalogoCuenta.DoesNotExist:
            messages.error(request, "El registro de catálogo seleccionado no existe.")
        except Exception as e:
            messages.error(request, f"Error al guardar la transacción: {e}")

    # Renderiza la plantilla con las cuentas si no es un POST o si hubo un error
    cuentas = CatalogoCuenta.objects.all()  # Obtener todas las cuentas
    return render(request, 'Form_transaccion.html', {'cuentas': cuentas})


def obtener_cuentas(request):
    # Cargar todas las cuentas desde el modelo `CatalogoCuenta`
    cuentas = CatalogoCuenta.objects.all()
    data = {}

    # Organizar las cuentas por tipo en un diccionario
    for cuenta in cuentas:
        tipo = cuenta.tipoDeCuenta
        if tipo not in data:
            data[tipo] = []
        data[tipo].append({
            'codigo': cuenta.codigo,
            'nombre': cuenta.nombreDeCuenta
        })
    # Devolver los datos en formato JSON
    return JsonResponse(data)

def libro_mayor(request):
    # Obtener todas las cuentas
    catalogo_cuentas = CatalogoCuenta.objects.all()

    total_debe = 0
    total_haber = 0
    total_saldo_deudor = 0
    total_saldo_acreedor = 0

    # Calcular el saldo deudor y acreedor para cada cuenta
    for cuenta in catalogo_cuentas:
        
        if cuenta.nombreDeCuenta=="Nuevo Capital Social":
            continue
        # Asegúrate de que los valores de 'debe' y 'haber' no sean nulos
        cuenta.debe = cuenta.debe if cuenta.debe is not None else 0
        cuenta.haber = cuenta.haber if cuenta.haber is not None else 0

        # Calcular el saldo según el tipo de cuenta
        if cuenta.tipoDeCuenta == "Activo":
            cuenta.saldo_deudor = cuenta.debe - cuenta.haber
            cuenta.saldo_acreedor = 0
        elif cuenta.tipoDeCuenta == "Pasivo":
            cuenta.saldo_acreedor = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = 0
        elif cuenta.tipoDeCuenta == "Patrimonio":
            cuenta.saldo_acreedor = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = 0
        elif cuenta.tipoDeCuenta == "Resultado Deudor":
            cuenta.saldo_deudor =   cuenta.debe - cuenta.haber
            cuenta.saldo_acreedor = 0
        elif cuenta.tipoDeCuenta == "Resultado Acreedor":
            cuenta.saldo_acreedor = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = 0 
        elif cuenta.tipoDeCuenta=="Cuenta de Cierre":
            resultado = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = resultado if resultado < 0 else 0
            cuenta.saldo_acreedor = resultado if resultado > 0 else 0
        else:
            # Si no hay tipo de cuenta, establecemos ambos saldos en 0
            cuenta.saldo_deudor = 0
            cuenta.saldo_acreedor = 0

        cuenta.save()  # Guardar los cambios en la cuenta

        # Sumar los valores a los totales
        total_debe += cuenta.debe
        total_haber += cuenta.haber
        total_saldo_deudor += cuenta.saldo_deudor
        total_saldo_acreedor += cuenta.saldo_acreedor

    context = {
        'catalogo_cuentas': catalogo_cuentas,  # Pasar todas las cuentas al contexto
        'total_debe': total_debe,
        'total_haber': total_haber,
        'total_saldo_deudor': total_saldo_deudor,
        'total_saldo_acreedor': total_saldo_acreedor,
    }

    return render(request, 'Libro_Mayor.html', context)

def obtener_montos_json(request):
    # Obtener todas las cuentas
    catalogo_cuentas = CatalogoCuenta.objects.all()

    total_debe = 0
    total_haber = 0
    total_saldo_deudor = 0
    total_saldo_acreedor = 0

    # Calcular el saldo deudor y acreedor para cada cuenta
    for cuenta in catalogo_cuentas:
        if cuenta.nombreDeCuenta == "Nuevo Capital Social":
            continue
        # Asegúrate de que los valores de 'debe' y 'haber' no sean nulos
        cuenta.debe = cuenta.debe if cuenta.debe is not None else 0
        cuenta.haber = cuenta.haber if cuenta.haber is not None else 0

        # Calcular el saldo según el tipo de cuenta
        if cuenta.tipoDeCuenta == "Activo":
            cuenta.saldo_deudor = cuenta.debe - cuenta.haber
            cuenta.saldo_acreedor = 0
        elif cuenta.tipoDeCuenta == "Pasivo":
            cuenta.saldo_acreedor = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = 0
        elif cuenta.tipoDeCuenta == "Patrimonio":
            cuenta.saldo_acreedor = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = 0
        elif cuenta.tipoDeCuenta == "Resultado Deudor":
            cuenta.saldo_deudor = cuenta.debe - cuenta.haber
            cuenta.saldo_acreedor = 0
        elif cuenta.tipoDeCuenta == "Resultado Acreedor":
            cuenta.saldo_acreedor = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = 0
        elif cuenta.tipoDeCuenta == "Cuenta de Cierre":
            resultado = cuenta.haber - cuenta.debe
            cuenta.saldo_deudor = resultado if resultado < 0 else 0
            cuenta.saldo_acreedor = resultado if resultado > 0 else 0
        else:
            # Si no hay tipo de cuenta, establecemos ambos saldos en 0
            cuenta.saldo_deudor = 0
            cuenta.saldo_acreedor = 0

        cuenta.save()  # Guardar los cambios en la cuenta

        # Sumar los valores a los totales
        total_debe += cuenta.debe
        total_haber += cuenta.haber
        total_saldo_deudor += cuenta.saldo_deudor
        total_saldo_acreedor += cuenta.saldo_acreedor

    data = {
        'catalogo_cuentas': list(catalogo_cuentas.values()),  # Convertir a lista de diccionarios
        'total_debe': total_debe,
        'total_haber': total_haber,
        'total_saldo_deudor': total_saldo_deudor,
        'total_saldo_acreedor': total_saldo_acreedor,
    }

    return JsonResponse(data)

def catalogo(request):
    return render(request, 'Catalogo_cuentas.html')
