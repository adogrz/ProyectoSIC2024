import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemacontable.settings')
django.setup()

from libromayor.models import CatalogoCuenta

cuentas = [
        #Activos
        {'codigo': '1101.01.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Caja General'},
        {'codigo': '1101.01.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Caja Chica'},
        {'codigo': '1101.02.01.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco de América Central, S.A.'},
        {'codigo': '1101.02.01.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco Cuscatlán de El Salvador, S.A.'},
        {'codigo': '1101.02.01.03', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco Davivienda, S.A.'},
        {'codigo': '1101.02.01.04', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco Agrícola, S.A.'},
        {'codigo': '1101.02.02.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco de América Central, S.A.'},
        {'codigo': '1101.02.02.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco Cuscatlán de El Salvador, S.A.'},
        {'codigo': '1101.02.02.03', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco Davivienda, S.A.'},
        {'codigo': '1101.02.02.04', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Banco Agrícola, S.A.'},
        {'codigo': '1102.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Cuentas por Cobrar Clientes'},
        {'codigo': '1102.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Préstamos a funcionarios y empleados'},
        {'codigo': '1102.03', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Documentos por cobrar'},
        {'codigo': '1103.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Estimación para cuentas incobrables'},
        {'codigo': '1104.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Seguros pagados por anticipado'},
        {'codigo': '1104.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Alquileres pagados por anticipado'},
        {'codigo': '1104.03', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Papelería y útiles'},
        {'codigo': '1104.04', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Contratos por servicios'},
        {'codigo': '1104.05', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Otros gastos pagados por anticipado'},
        {'codigo': '1105.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Pago a cuenta ISR'},
        {'codigo': '1106.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'IVA credito fiscal'},
        {'codigo': '1201.01.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Mobiliario y equipo de Oficina'},
        {'codigo': '1201.01.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Equipo de cómputo'},
        {'codigo': '1201.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Herramientas y equipos'},
        {'codigo': '1201.03.01.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Depreciación acumulada de Mobiliario y equipo de oficina'},
        {'codigo': '1201.03.01.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Depreciación acumulada de equipo de cómputo'},
        {'codigo': '1201.03.01.03', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Depreciación acumulada de otros equipos'},
        {'codigo': '1201.03.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Depr. acum. revaluación mobiliario y equipo'},
        {'codigo': '1202.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Patentes y marcas'},
        {'codigo': '1202.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Licencias y concesiones'},
        {'codigo': '1202.03', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Programas y sistemas'},
        {'codigo': '1202.04', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Amortización acumulada de activos intangibles'},
        {'codigo': '1202.05', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Amortización acumulada de patentes y marcas'},
        {'codigo': '1202.06', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Amortización acumulada de licencias y concesiones'},
        {'codigo': '1202.07', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Amortización acumulada de programas y sistemas'},
        {'codigo': '1203.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Clientes / Largo plazo'},
        {'codigo': '1204.01', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Crédito ISR años anteriores'},
        {'codigo': '1204.02', 'tipoDeCuenta': 'Activo', 'nombreDeCuenta': 'Activo por Impuesto S/ Renta Diferido'},

        #Pasivo
        {'codigo': '2101.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Sobregiros bancarios'},
        {'codigo': '2101.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Préstamos bancarios (porción a corto plazo)'},
        {'codigo': '2101.03', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Préstamos personales (porción a corto plazo)'},
        {'codigo': '2102.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Documentos por pagar'},
        {'codigo': '2103.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Cuota patronal ISSS'},
        {'codigo': '2103.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Cuota patronal AFP'},
        {'codigo': '2103.03', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'IVA por pagar'},
        {'codigo': '2103.04', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Pago a cuenta'},
        {'codigo': '2103.05', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Impuestos municipales'},
        {'codigo': '2103.06', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Otros impuestos por pagar'},
        {'codigo': '2103.07', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Intereses por pagar'},
        {'codigo': '2103.08', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Honorarios por pagar'},
        {'codigo': '2103.09', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Alquileres por pagar'},
        {'codigo': '2103.10', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Anticipos de clientes'},
        {'codigo': '2103.11', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Provisiones de caja chica'},
        {'codigo': '2103.11.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Caja chica por reintegrar'},
        {'codigo': '2103.11.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Provisiones de arrendamiento'},
        {'codigo': '2103.12', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Otras cuentas por pagar'},
        {'codigo': '2104.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Cotización ISSS / Salud'},
        {'codigo': '2104.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Cotización a fondo de pensiones'},
        {'codigo': '2104.02.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'ISSS provisional'},
        {'codigo': '2104.02.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'AFP Crecer'},
        {'codigo': '2104.02.03', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'AFP Confía'},
        {'codigo': '2104.03', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Retención de Impuesto sobre la Renta'},
        {'codigo': '2104.04', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Retención F. S. V'},
        {'codigo': '2104.05', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Órdenes de descuentos - bancos y otras financieras'},
        {'codigo': '2104.06', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Procuraduría General de la República'},
        {'codigo': '2104.07', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Otras retenciones'},
        {'codigo': '2105.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Sueldos por pagar'},
        {'codigo': '2105.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Comisiones por pagar'},
        {'codigo': '2105.03', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Horas extras por pagar'},
        {'codigo': '2105.04', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Vacaciones por pagar'},
        {'codigo': '2105.05', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Aguinaldos por pagar'},
        {'codigo': '2105.06', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Gratificaciones y bonificaciones por pagar'},
        {'codigo': '2105.07', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Indemnizaciones por pagar'},
        {'codigo': '2105.08', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Bonificaciones por pagar'},
        {'codigo': '2105.09', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Otros beneficios a empleados por pagar'},
        {'codigo': '2106.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Impuesto sobre la Renta - Corriente'},
        {'codigo': '2106.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Pago a cuenta'},
        {'codigo': '2107.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'IVA - débito fiscal'},
        {'codigo': '2201.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Préstamos bancarios (Porción a largo plazo)'},
        {'codigo': '2201.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Préstamos personales (Porción a largo plazo)'},
        {'codigo': '2202.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Indemnizaciones por pagar'},
        {'codigo': '2202.02', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Otras prestaciones por pagar a largo plazo'},
        {'codigo': '2203.01', 'tipoDeCuenta': 'Pasivo', 'nombreDeCuenta': 'Pasivo por Impuesto sobre la Renta diferido'},

        #Patrimonio
        {'codigo': '3101.01', 'tipoDeCuenta': 'Patrimonio', 'nombreDeCuenta': 'Capital social'},
        {'codigo': '3102.01', 'tipoDeCuenta': 'Patrimonio', 'nombreDeCuenta': 'Reserva legal'},
        {'codigo': '3103.01', 'tipoDeCuenta': 'Patrimonio', 'nombreDeCuenta': 'Superavit por revaluaciones'},
        {'codigo': '3201.01', 'tipoDeCuenta': 'Patrimonio', 'nombreDeCuenta': 'Utilidades de ejercicios anteriores'},
        {'codigo': '3202.01', 'tipoDeCuenta': 'Patrimonio', 'nombreDeCuenta': 'Utilidad del presente ejercicio'},
        {'codigo': '3203.01', 'tipoDeCuenta': 'Patrimonio', 'nombreDeCuenta': 'Déficit de ejercicios anteriores'},
        {'codigo': '3204.01', 'tipoDeCuenta': 'Patrimonio', 'nombreDeCuenta': 'Déficit del presente ejercicio'},

        #Cuentas de resultado deudor
        {'codigo': '4101.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Costo de servicio'},
        {'codigo': '4101.01.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Costos por servicios'},
        {'codigo': '4101.01.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'CIF Control (Real)'},
        {'codigo': '4102.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Gastos de personal'},
        {'codigo': '4102.01.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Salarios'},
        {'codigo': '4102.01.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Vacaciones'},
        {'codigo': '4102.01.03', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Aguinaldos'},
        {'codigo': '4102.01.04', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Bonificaciones y gratificaciones'},
        {'codigo': '4102.01.05', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Horas extras'},
        {'codigo': '4102.01.06 ', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Indemnizaciones'},
        {'codigo': '4102.01.07', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Viáticos'},
        {'codigo': '4102.01.08', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Cuota patronal seguridad social ISSS'},
        {'codigo': '4102.01.09', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Cuota patronal fondo de pensiones AFP'},
        {'codigo': '4102.01.10', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Comisiones, premios e incentivos'},
        {'codigo': '4102.01.11', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Otros gastos del personal'},
        {'codigo': '4102.02.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Mantenimiento de Mobiliario Equipo De Oficina'},
        {'codigo': '4102.02.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Otros gastos por mantenimiento'},
        {'codigo': '4102.03.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Servicio de agua'},
        {'codigo': '4102.03.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Servicio de energía eléctrica'},
        {'codigo': '4102.03.03', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Servicio de internet'},
        {'codigo': '4102.03.04', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Publicidad y promoción'},
        {'codigo': '4102.03.05', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Otros servicios'},
        {'codigo': '4102.04.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Honorarios legales'},
        {'codigo': '4102.04.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Honorarios contables'},
        {'codigo': '4102.04.03', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Honorarios de auditoría'},
        {'codigo': '4102.04.04', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Honorarios por servicios administrativos'},
        {'codigo': '4102.04.05', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Otros honorarios'},
        {'codigo': '4102.05.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Depreciación de Mobiliario y Equipo de Oficina'},
        {'codigo': '4102.05.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Depreciación de Herramientas y Equipo Pequeño'},
        {'codigo': '4102.06.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Amortización de activos intangibles'},
        {'codigo': '4102.07.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Seguro de vida y medico'},
        {'codigo': '4102.07.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Seguro de activos'},
        {'codigo': '4102.08.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Atención a empleados'},
        {'codigo': '4102.08.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Atención a Clientes'},
        {'codigo': '4102.08.03', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Cursos de capacitación a empleados'},
        {'codigo': '4102.08.04', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Otras atenciones a clientes y empleados'},
        {'codigo': '4201.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Intereses sobre préstamos'},
        {'codigo': '4201.02', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Comisiones'},
        {'codigo': '4201.03', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Seguros'},
        {'codigo': '4201.04', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Impuesto a las Operaciones Financieras'},
        {'codigo': '4202.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Pérdida en venta o retiro de activos fijos'},
        {'codigo': '4203.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Gastos por deterioro en el valor de activos'},
        {'codigo': '4204.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Pérdidas por siniestros'},
        {'codigo': '4205.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Gastos de ejercicios anteriores'},
        {'codigo': '4206.01', 'tipoDeCuenta': 'Resultado Deudor', 'nombreDeCuenta': 'Otros Gastos no Clasificados'},

        #Resultado Acreedor
        {'codigo': '5101.01', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Ventas locales'},
        {'codigo': '5101.01.01', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Ventas a consumidor final'},
        {'codigo': '5101.02', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Descuentos sobre ventas'},
        {'codigo': '5101.03', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Penalizaciones sobre ventas'},
        {'codigo': '5201.01', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Intereses bancarios'},
        {'codigo': '5201.02', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Otros Intereses'},
        {'codigo': '5202.01', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Ganancia en venta de activos fijos'},
        {'codigo': '5203.01', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Indemnizaciones por siniestros'},
        {'codigo': '5204.01', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Comisiones'},
        {'codigo': '5204.02', 'tipoDeCuenta': 'Resultado Acreedor', 'nombreDeCuenta': 'Otros productos'},

        #Cuenta de cierre
        {'codigo': '6101.01', 'tipoDeCuenta': 'Cuenta de Cierre', 'nombreDeCuenta': 'Pérdidas y ganancias'},
        {'codigo': '6101.02', 'tipoDeCuenta': 'Cuenta de Cierre', 'nombreDeCuenta': 'Variación de CIF'}

]

for cuenta in cuentas:
    CatalogoCuenta.objects.create(**cuenta)


print("Cuentas agregadas exitosamente")