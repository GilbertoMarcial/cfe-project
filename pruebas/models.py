# -*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class EPS(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'EPS'
        verbose_name_plural = 'EPS'
        ordering = ['name', ]


class Subgerencia(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    eps = models.ForeignKey(EPS, on_delete=models.CASCADE, verbose_name='EPS')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subgerencia'
        verbose_name_plural = 'Subgerencias'
        ordering = ['name', ]

    @property
    def get_eps(self):
        return self.eps.name


class Central(models.Model):
    alias = models.CharField(max_length=50, verbose_name='Clave', unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    subgerencia = models.ForeignKey(Subgerencia, on_delete=models.CASCADE, verbose_name='Subgerencia')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Central'
        verbose_name_plural = 'Centrales'
        ordering = ['name', ]

    @property
    def get_subgerencia(self):
        return self.subgerencia.name


class Unidad(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    central = models.ForeignKey(Central, on_delete=models.CASCADE, verbose_name='Central')

    def __str__(self):
        return '%s [%s]' % (self.name, self.central.name)

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['name', ]

    @property
    def get_central(self):
        return self.central.name


class Equipo(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    n_serie = models.CharField(max_length=50, verbose_name='Número de Serie', unique=True)
    ano_puesta_servicio = models.IntegerField(verbose_name='Año de Puesta en Servicio')
    condicion_operacion = models.TextField(verbose_name='Condición de Operación', blank=True)
    razon_fuera_servicio = models.TextField(verbose_name='Razón Fuera de Servicio', blank=True)
    problematica_operativa = models.TextField(verbose_name='Problemática Operativa', blank=True)
    indice_condicion = models.TextField(verbose_name='Índice de Condición', blank=True)
    observaciones = models.TextField(verbose_name='Observaciones', blank=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    unidades = models.ManyToManyField(Unidad, verbose_name='Unidades')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['name', ]


class Trafo(Equipo):
    n_devanados = models.IntegerField(verbose_name='Número de Devanados')
    kv_nominal_at = models.FloatField(verbose_name='KV Nominal AT')
    kv_nominal_bt = models.FloatField(verbose_name='KV Nominal BT')
    tension_kv = models.FloatField(verbose_name='Tensión KV')
    elevacion_temperatura = models.FloatField(verbose_name='Elevación de Temperatura')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Trafo'
        verbose_name_plural = 'Trafos'
        ordering = ['name', ]
