# Generated by Django 5.0.1 on 2024-02-01 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('n_serie', models.CharField(max_length=50, unique=True, verbose_name='Número de Serie')),
                ('ano_puesta_servicio', models.IntegerField(verbose_name='Año de Puesta en Servicio')),
                ('condicion_operacion', models.TextField(verbose_name='Condición de Operación')),
                ('razon_fuera_servicio', models.TextField(verbose_name='Razón Fuera de Servicio')),
                ('problematica_operativa', models.TextField(verbose_name='Problemática Operativa')),
                ('indice_condicion', models.TextField(verbose_name='Índice de Condición')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Central',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50, unique=True, verbose_name='Clave')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('subgerencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.subgerencia', verbose_name='Subgerencia')),
            ],
            options={
                'verbose_name': 'Central',
                'verbose_name_plural': 'Centrales',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('central', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.central', verbose_name='Central')),
                ('equipos', models.ManyToManyField(to='pruebas.equipo', verbose_name='Equipos')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='equipo',
            name='unidades',
            field=models.ManyToManyField(to='pruebas.unidad', verbose_name='Unidades'),
        ),
    ]
