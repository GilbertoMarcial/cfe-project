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
