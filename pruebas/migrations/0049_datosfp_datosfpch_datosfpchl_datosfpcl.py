# Generated by Django 5.0.1 on 2024-02-19 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0048_resistenciaaislamientochl_resistenciaaislamientocht_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosFP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_referencia', models.FloatField(verbose_name='FP Referencia')),
                ('corriente_ma', models.FloatField(verbose_name='Corriente (mA)')),
                ('watts', models.FloatField(verbose_name='Watts')),
                ('fp', models.FloatField(verbose_name='FP')),
                ('p_fp_placa', models.FloatField(verbose_name='% FP Placa')),
                ('velocidad_cambio_fp_placa', models.FloatField(verbose_name='Velocidad de Cambio FP Placa')),
                ('aceleracion_fp_placa', models.FloatField(verbose_name='Aceleración FP Placa')),
                ('tension_prueba', models.FloatField(verbose_name='Tensión de Prueba')),
                ('electrica_trafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.electricatrafo', verbose_name='Prueba Eléctrica de Trafos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatosFPCH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_referencia', models.FloatField(verbose_name='FP Referencia')),
                ('corriente_ma', models.FloatField(verbose_name='Corriente (mA)')),
                ('watts', models.FloatField(verbose_name='Watts')),
                ('fp', models.FloatField(verbose_name='FP')),
                ('p_fp_placa', models.FloatField(verbose_name='% FP Placa')),
                ('velocidad_cambio_fp_placa', models.FloatField(verbose_name='Velocidad de Cambio FP Placa')),
                ('aceleracion_fp_placa', models.FloatField(verbose_name='Aceleración FP Placa')),
                ('electrica_trafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.electricatrafo', verbose_name='Prueba Eléctrica de Trafos')),
            ],
            options={
                'verbose_name': 'Datos Factor de Potencia - CH',
                'verbose_name_plural': 'Datos Factores de Potencia - CH',
            },
        ),
        migrations.CreateModel(
            name='DatosFPCHL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_referencia', models.FloatField(verbose_name='FP Referencia')),
                ('corriente_ma', models.FloatField(verbose_name='Corriente (mA)')),
                ('watts', models.FloatField(verbose_name='Watts')),
                ('fp', models.FloatField(verbose_name='FP')),
                ('p_fp_placa', models.FloatField(verbose_name='% FP Placa')),
                ('velocidad_cambio_fp_placa', models.FloatField(verbose_name='Velocidad de Cambio FP Placa')),
                ('aceleracion_fp_placa', models.FloatField(verbose_name='Aceleración FP Placa')),
                ('electrica_trafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.electricatrafo', verbose_name='Prueba Eléctrica de Trafos')),
            ],
            options={
                'verbose_name': 'Datos Factor de Potencia - CHL',
                'verbose_name_plural': 'Datos Factores de Potencia - CHL',
            },
        ),
        migrations.CreateModel(
            name='DatosFPCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_referencia', models.FloatField(verbose_name='FP Referencia')),
                ('corriente_ma', models.FloatField(verbose_name='Corriente (mA)')),
                ('watts', models.FloatField(verbose_name='Watts')),
                ('fp', models.FloatField(verbose_name='FP')),
                ('p_fp_placa', models.FloatField(verbose_name='% FP Placa')),
                ('velocidad_cambio_fp_placa', models.FloatField(verbose_name='Velocidad de Cambio FP Placa')),
                ('aceleracion_fp_placa', models.FloatField(verbose_name='Aceleración FP Placa')),
                ('electrica_trafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.electricatrafo', verbose_name='Prueba Eléctrica de Trafos')),
            ],
            options={
                'verbose_name': 'Datos Factor de Potencia - CL',
                'verbose_name_plural': 'Datos Factores de Potencia - CL',
            },
        ),
    ]