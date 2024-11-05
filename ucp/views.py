from django.shortcuts import render

def costo_ucp(request):
    return render(request, 'costo_ucp.html')

def costo_venta(request):
    return render(request, 'costo_venta.html')
