# Generated by Django 5.0.1 on 2024-02-06 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0013_prueba_electricatrafo_respuestafrecuencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electricatrafo',
            name='prueba',
        ),
        migrations.RemoveField(
            model_name='electricatrafo',
            name='trafo',
        ),
        migrations.RemoveField(
            model_name='respuestafrecuencia',
            name='electrica_trafo',
        ),
        migrations.DeleteModel(
            name='Prueba',
        ),
        migrations.DeleteModel(
            name='ElectricaTrafo',
        ),
        migrations.DeleteModel(
            name='RespuestaFrecuencia',
        ),
    ]
