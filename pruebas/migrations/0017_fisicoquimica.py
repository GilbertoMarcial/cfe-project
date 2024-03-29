# Generated by Django 5.0.1 on 2024-02-07 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0016_electricatrafo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisicoQuimica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prueba', models.DateField(verbose_name='Fecha de Prueba')),
                ('exploratoria_aceite', models.FloatField(verbose_name='Prueba Exploratoria de Aceite')),
                ('analisis_gases_disueltos', models.FloatField(verbose_name='Análisis de Gases Disueltos')),
                ('contenido_humedad', models.FloatField(verbose_name='Contenido de Humedad')),
                ('fp_liquido_25c', models.FloatField(verbose_name='FP Líquido a 25°C')),
                ('fp_liquido_100c', models.FloatField(verbose_name='PF Líquido a 100°C')),
                ('contenido_inhibidor_oxidacion', models.FloatField(verbose_name='Contenido de Inhibidor de Oxidación')),
                ('compuestos_furanicos', models.FloatField(verbose_name='Compuestos Furánicos')),
                ('rigidez_dielectrica', models.FloatField(verbose_name='Rigidez Dieléctrica')),
                ('factor_potencia', models.FloatField(verbose_name='Factor de Potencia')),
                ('tension_interfacial', models.FloatField(verbose_name='Tensión Interfacial')),
                ('color', models.FloatField(verbose_name='Color')),
                ('examinacion_visual', models.TextField(blank=True, verbose_name='Examinación Visual')),
                ('nivel_neutralizacion', models.FloatField(verbose_name='Nivel de Neutralización')),
                ('contenido_agua', models.FloatField(verbose_name='Contenido de Agua')),
                ('contenido_inhibidor_oxidacion_especifico', models.FloatField(verbose_name='Contenido de Inhibidor de Oxidación Específico')),
                ('azufre_corrosivo', models.FloatField(verbose_name='Azufre Corrosivo')),
                ('humedad_resiudal', models.FloatField(verbose_name='Humedad Residual')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.prueba', verbose_name='Prueba')),
            ],
            options={
                'verbose_name': 'Prueba Físico Química',
                'verbose_name_plural': 'Pruebas Físico Químicas',
                'ordering': ['fecha_prueba', 'prueba__matricula', 'prueba__trafo', 'prueba__trafo__unidades', 'prueba__trafo__unidades__central'],
            },
        ),
    ]
