from django.shortcuts import render
from libromayor.models import CatalogoCuenta


#cambio de patriomonio o estado de capital
def cambio_patrimonial(request):
    #obtener todas las cuentas de tipo patrimonio
    catalogo_cuentas = (CatalogoCuenta.objects.filter(tipoDeCuenta="Patrimonio")
                        |CatalogoCuenta.objects.filter(codigo="4202.01")
                        |CatalogoCuenta.objects.filter(codigo="4203.01")
                        |CatalogoCuenta.objects.filter(codigo="4204.01")
                        |CatalogoCuenta.objects.filter(codigo="4205.01")
                        |CatalogoCuenta.objects.filter(codigo="6101.01")
                        |CatalogoCuenta.objects.filter(codigo="6101.02")
                        |CatalogoCuenta.objects.filter(codigo="7101"))
    total_saldo_deudor = 0
    total_saldo_acreedor = 0
    nuevo_capital_social=0

    #calcular el saldo deudor y acreedor para cada cuenta
    for cuenta in catalogo_cuentas:
        if cuenta.nombreDeCuenta=="Nuevo Capital Social":
            continue
        #asegurarse de que los valores de 'debe' y 'haber' no sean nulos
        cuenta.saldo_deudor = cuenta.saldo_deudor if cuenta.saldo_deudor is not None else 0
        cuenta.saldo_acreedor = cuenta.saldo_acreedor if cuenta.saldo_acreedor is not None else 0
        

        #sumar los valores a los totales
        total_saldo_deudor += cuenta.saldo_deudor
        total_saldo_acreedor += cuenta.saldo_acreedor

        #calcular el nuevo capital social
        nuevo_capital_social=total_saldo_acreedor-total_saldo_deudor

        cuenta_nuevo_capital=CatalogoCuenta.objects.filter(codigo="7101").first()
        if cuenta_nuevo_capital:
            cuenta_nuevo_capital.saldo_acreedor=nuevo_capital_social
            cuenta_nuevo_capital.save()

    context = {
        'catalogo_cuentas': catalogo_cuentas,
        'total_saldo_deudor': total_saldo_deudor,
        'total_saldo_acreedor': total_saldo_acreedor,
        'nuevo_capital_social':nuevo_capital_social
    }

 


    return render(request, 'cambio_patrimonial.html', context)

    