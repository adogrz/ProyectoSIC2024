"""
URL configuration for sistemacontable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from costos import views as costos_views
from ucp import views as ucp_views
from libromayor import views as libro_views
from estadosfinancieros import views as estados_views


def inicio_view(request):
    return render(request, 'inicio.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
    path('lista_puestos/', costos_views.lista_puestos, name='lista_puestos'),
    path('agregar_puesto/', costos_views.agregar_puesto, name='agregar_puesto'),
    path('calcular_costo_mano_obra/', costos_views.calcular_costo_mano_obra, name='calcular_costo_mano_obra'),
    path('obtener_sueldo_por_hora/<int:puesto_id>/', costos_views.obtener_sueldo_por_hora,
         name='obtener_sueldo_por_hora'),
    path('calcular_costos_indirectos/', costos_views.calcular_costos_indirectos, name='calcular_costos_indirectos'),
    # UCP
    path('costo_ucp/', ucp_views.costo_ucp, name='costo_ucp'),
    path('costo_venta/', ucp_views.costo_venta, name='costo_venta'),

    # Libro Mayor, catalogo y transacciones
    path('transacciones/', libro_views.transaccion, name="formtransaccion"),
    path('obtener-cuentas/', libro_views.obtener_cuentas, name='obtener_cuentas'),
    path('libromayor/', libro_views.obtener_montos, name="libro_mayor"),
    path('catalogo/', libro_views.catalogo, name="catalogo"),

    #Estados Financieros
    path('cambio_patrimonial/', estados_views.cambio_patrimonial, name='cambio_patrimonial'),


    #balance general
    path('estado_resultados/', estados_views.estado_resultados, name="estado_resultados"),
    # balance general
    path('balancegeneral/', estados_views.balance_general, name="balance_general")
]
