# Generated by Django 5.0.1 on 2024-02-16 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0043_delete_resistenciaaislamiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestafrecuencia',
            name='diferencia_realizacion_prueba',
            field=models.FloatField(blank=True, null=True, verbose_name='Diferencia de Realización de Prueba'),
        ),
        migrations.AddField(
            model_name='respuestafrecuencia',
            name='respuesta_frecuencia_dielectrica',
            field=models.FloatField(blank=True, null=True, verbose_name='Respuesta de Frecuencia Dieléctrica'),
        ),
        migrations.CreateModel(
            name='ResistenciaAislamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_a_30_seg', models.FloatField(verbose_name='Resistencia de Aislamiento a 30 seg')),
                ('r_a_1_min', models.FloatField(verbose_name='Resistencia de Aislamiento a 1 min')),
                ('r_a_10_min', models.FloatField(verbose_name='Resistencia de Aislamiento a 10 min')),
                ('temperatura_prueba', models.FloatField(verbose_name='Temperatura de Prueba')),
                ('factor_k', models.FloatField(blank=True, null=True, verbose_name='Factor K')),
                ('indice_absorcion', models.FloatField(blank=True, null=True, verbose_name='Índice de Absorción')),
                ('indice_polarizacion', models.FloatField(blank=True, null=True, verbose_name='Índice de Polarización')),
                ('electrica_trafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.electricatrafo', verbose_name='Prueba Eléctrica de Trafos')),
            ],
            options={
                'verbose_name': 'Resistencia de Aislamiento',
                'verbose_name_plural': 'Resistencias de Aislamiento',
            },
        ),
    ]
