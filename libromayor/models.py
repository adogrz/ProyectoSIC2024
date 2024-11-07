from django.db import models


class CatalogoCuenta(models.Model):
    idCuenta = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=15)
    tipoDeCuenta = models.CharField(max_length=50)
    nombreDeCuenta = models.CharField(max_length=100)
    debe = models.FloatField(null=True, blank=True)
    haber = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombreDeCuenta}"
