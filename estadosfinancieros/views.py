from django.shortcuts import render
from libromayor.models import CatalogoCuenta
from django.db.models import Q


def obtener_saldo(codigo, naturaleza):
    cuenta = CatalogoCuenta.objects.filter(codigo=codigo).first()
    if cuenta:
        return cuenta.saldo_deudor if naturaleza == 'deudora' else cuenta.saldo_acreedor
    return 0


def estado_resultados(request):
    # -------------- Ventas Netas ---------------
    ventas_consumidor_final = obtener_saldo('5101.01.01', 'acreedora')
    descuentos_sobre_ventas = obtener_saldo('5101.02', 'acreedora')
    penalizaciones_sobre_ventas = obtener_saldo('5101.03', 'acreedora')
    ventas_netas = ventas_consumidor_final - descuentos_sobre_ventas - penalizaciones_sobre_ventas

    # -------------- Costo de Ventas ----------
    costos_por_servicios = obtener_saldo('4101.01.01', 'deudora')
    cif_control = obtener_saldo('4101.01.02', 'deudora')
    costo_ventas = costos_por_servicios + cif_control

    # ------- Utilidad Bruta --------------
    utilidad_bruta = ventas_netas - costo_ventas

    cuenta_perdidas_ganancias = CatalogoCuenta.objects.filter(codigo="6101.01").first()
    if cuenta_perdidas_ganancias:
        if utilidad_bruta > 0:
            cuenta_perdidas_ganancias.haber = utilidad_bruta
            cuenta_perdidas_ganancias.debe = 0
        else:
            cuenta_perdidas_ganancias.debe = utilidad_bruta
            cuenta_perdidas_ganancias.haber = 0
        cuenta_perdidas_ganancias.save()
    else:
        print("No se encontró la cuenta 6101.01")

    # Gastos Administrativos
    salarios = obtener_saldo('4102.01.01', 'deudora')
    vacaciones = obtener_saldo('4102.01.02', 'deudora')
    aguinaldo = obtener_saldo('4102.01.03', 'deudora')
    bonificicaciones = obtener_saldo('4102.01.04', 'deudora')
    horas_extra = obtener_saldo('4102.01.05', 'deudora')
    indemnizaciones_siniestros = obtener_saldo('4102.01.06', 'deudora')
    viaticos = obtener_saldo('4102.01.07', 'deudora')
    cuota_patronal_isss = obtener_saldo('4102.01.08', 'deudora')
    cuota_patronal_afp = obtener_saldo('4102.01.09', 'deudora')
    comisiones_premios = obtener_saldo('4102.01.10', 'deudora')
    otros_gastos_personal = obtener_saldo('4102.01.11', 'deudora')
    gastos_administrativos = (
                salarios + vacaciones + aguinaldo + bonificicaciones + horas_extra + indemnizaciones_siniestros + viaticos
                + cuota_patronal_isss + cuota_patronal_afp + comisiones_premios + otros_gastos_personal)

    # Gastos de mantenimiento
    gastos_mantenimiento = (obtener_saldo('4102.02.01', 'deudora') + obtener_saldo('4102.02.02', 'deudora'))

    # Gastos por servicios publicos y privados
    gastos_servicio_agua = obtener_saldo('4102.03.01', 'deudora')
    gastos_servicio_energia_electrica = obtener_saldo('4102.03.02', 'deudora')
    gastos_servico_internet = obtener_saldo('4102.03.03', 'deudora')
    gastos_publicidad = obtener_saldo('4102.03.04', 'deudora')
    gastos_otros_servicios = obtener_saldo('4102.03.05', 'deudora')
    servicios_publicos = (gastos_servicio_agua + gastos_servicio_energia_electrica + gastos_servico_internet
                          + gastos_publicidad + gastos_otros_servicios)
    honorarios_profesionales = (obtener_saldo('4102.04.01', 'deudora')
                                + obtener_saldo('4102.04.02', 'deudora')
                                + obtener_saldo('4102.04.03', 'deudora')
                                + obtener_saldo('4102.04.04', 'deudora')
                                + obtener_saldo('4102.04.05', 'deudora'))
    gastos_depreciacion = (obtener_saldo('4102.05.01', 'deudora') + obtener_saldo('4102.05.02', 'deudora'))
    amortizacion = obtener_saldo('4102.06.01', 'deudora')
    seguros = (obtener_saldo('4102.07.01', 'deudora') + obtener_saldo('4102.07.02', 'deudora'))
    gastos_clientes_empleados = (obtener_saldo('4102.08.01', 'deudora')
                                 + obtener_saldo('4102.08.02', 'deudora')
                                 + obtener_saldo('4102.08.03', 'deudora')
                                 + obtener_saldo('4102.08.04', 'deudora')
                                 + obtener_saldo('4102.08.05', 'deudora'))

    # ----- Gastos de operación -----
    gastos_operacion = (gastos_administrativos + gastos_mantenimiento + servicios_publicos + honorarios_profesionales
                        + gastos_depreciacion + amortizacion + seguros + gastos_clientes_empleados)

    # --------- Utilidad en Operación --------
    utilidad_operacion = utilidad_bruta - gastos_operacion

    # --------- Otros Productos ---------
    productos_financieros = obtener_saldo('5201.01', 'acreedora') + obtener_saldo('5201.02', 'acreedora')
    ganancia_venta_activos = obtener_saldo('5202.01', 'acreedora')
    indemnizaciones_siniestros = obtener_saldo('5203.01', 'acreedora')
    otros_productos = obtener_saldo('5204.01', 'acreedora') + obtener_saldo('5204.02', 'acreedora')
    total_productos = productos_financieros + ganancia_venta_activos + indemnizaciones_siniestros + otros_productos

    # --------- Otros gastos ----------
    gastos_financieros = (obtener_saldo('4201.01', 'deudora') + obtener_saldo('4201.02', 'deudora')
                          + obtener_saldo('4201.03', 'deudora') + obtener_saldo('4201.04', 'deudora'))
    perdidas_retiro_activos = obtener_saldo('4202.01', 'deudora')
    gastos_deterioro_activos = obtener_saldo('4203.01', 'deudora')
    gastos_no_clasificados = obtener_saldo('4206.01', 'deudora')
    otros_gastos = gastos_financieros + perdidas_retiro_activos + gastos_deterioro_activos + gastos_no_clasificados

    # ------- Utilidad Antes de Impuestos -------------
    utilidad_antes_impuestos = utilidad_operacion + total_productos - otros_gastos

    # Impuesto sobre la renta (30% de la Utilidad Antes de Impuestos)
    impuesto_renta = utilidad_antes_impuestos * 0.30

    # Utilidad Neta
    utilidad_neta = utilidad_antes_impuestos - impuesto_renta

    # Pasar los resultados al template
    context = {
        'ventas_netas': ventas_netas,
        'costo_ventas': costo_ventas,
        'utilidad_bruta': utilidad_bruta,
        'gastos_operacion': gastos_operacion,
        'utilidad_operacion': utilidad_operacion,
        'total_productos': total_productos,
        'otros_gastos': otros_gastos,
        'utilidad_antes_impuestos': utilidad_antes_impuestos,
        'impuesto_renta': impuesto_renta,
        'utilidad_neta': utilidad_neta,
    }

    return render(request, 'estado_resultados.html', context)


# cambio de patriomonio o estado de capital
def cambio_patrimonial(request):
    # obtener todas las cuentas de tipo patrimonio
    catalogo_cuentas = (CatalogoCuenta.objects.filter(tipoDeCuenta="Patrimonio")
                        | CatalogoCuenta.objects.filter(codigo="4202.01")
                        | CatalogoCuenta.objects.filter(codigo="4203.01")
                        | CatalogoCuenta.objects.filter(codigo="4204.01")
                        | CatalogoCuenta.objects.filter(codigo="4205.01")
                        | CatalogoCuenta.objects.filter(codigo="6101.01")
                        | CatalogoCuenta.objects.filter(codigo="6101.02")
                        | CatalogoCuenta.objects.filter(codigo="7101"))
    total_saldo_deudor = 0
    total_saldo_acreedor = 0
    nuevo_capital_social = 0

    # calcular el saldo deudor y acreedor para cada cuenta
    for cuenta in catalogo_cuentas:
        if cuenta.nombreDeCuenta == "Nuevo Capital Social":
            continue
        # asegurarse de que los valores de 'debe' y 'haber' no sean nulos
        cuenta.saldo_deudor = cuenta.saldo_deudor if cuenta.saldo_deudor is not None else 0
        cuenta.saldo_acreedor = cuenta.saldo_acreedor if cuenta.saldo_acreedor is not None else 0

        # sumar los valores a los totales
        total_saldo_deudor += cuenta.saldo_deudor
        total_saldo_acreedor += cuenta.saldo_acreedor

        # calcular el nuevo capital social
        nuevo_capital_social = total_saldo_acreedor - total_saldo_deudor

        cuenta_nuevo_capital = CatalogoCuenta.objects.filter(codigo="7101").first()
        if cuenta_nuevo_capital:
            cuenta_nuevo_capital.saldo_acreedor = nuevo_capital_social
            cuenta_nuevo_capital.save()

    context = {
        'catalogo_cuentas': catalogo_cuentas,
        'total_saldo_deudor': total_saldo_deudor,
        'total_saldo_acreedor': total_saldo_acreedor,
        'nuevo_capital_social': nuevo_capital_social
    }

    return render(request, 'cambio_patrimonial.html', context)


def balance_general(request):
    # Obtener todas las cuentas de tipo Activo y Pasivo, y la cuenta con nombre "Capital Social"
    catalogo_cuentas = CatalogoCuenta.objects.filter(Q(tipoDeCuenta__in=["Activo", "Pasivo"]) | Q(codigo="7101"))

    total_debe = 0
    total_haber = 0
    saldo_deudor_7101 = 0
    saldo_acreedor_7101 = 0
    cuenta_7101 = None

    # Calcular el total de debe y haber solo para las cuentas seleccionadas
    for cuenta in catalogo_cuentas:
        # Asegúrate de que los valores de 'debe' y 'haber' no sean nulos
        cuenta.debe = cuenta.debe if cuenta.debe is not None else 0
        cuenta.haber = cuenta.haber if cuenta.haber is not None else 0
        if cuenta.codigo == "7101":
            # Obtener el saldo deudor y acreedor de la cuenta 7101
            saldo_deudor_7101 = cuenta.saldo_deudor if cuenta.saldo_deudor is not None else 0
            saldo_acreedor_7101 = cuenta.saldo_acreedor if cuenta.saldo_acreedor is not None else 0
            cuenta_7101 = cuenta
            # Sumar los saldos en lugar de debe y haber
            total_debe += saldo_deudor_7101
            total_haber += saldo_acreedor_7101
        else:
            # Sumar los valores a los totales
            total_debe += cuenta.debe
            total_haber += cuenta.haber

    context = {
        'catalogo_cuentas': [cuenta for cuenta in catalogo_cuentas if cuenta.codigo != "7101"],  # Excluir la cuenta 7101
        'cuenta_7101': cuenta_7101,
        'total_debe': total_debe,
        'total_haber': total_haber,
        'saldo_deudor_7101': saldo_deudor_7101,
        'saldo_acreedor_7101': saldo_acreedor_7101,
    }

    return render(request, 'Balance_general.html', context)
