# Generated by Django 5.1.3 on 2024-11-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libromayor', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogocuenta',
            name='saldo_acreedor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='catalogocuenta',
            name='saldo_deudor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
