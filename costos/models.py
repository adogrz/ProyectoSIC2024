from django.db import models


class PuestoTrabajo(models.Model):
    nombre = models.CharField(max_length=100)
    sueldo_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    sueldo_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
    es_administrativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
