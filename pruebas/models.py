# -*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
import math


# EPS, Subgerencia, Central, Unidad y Equipo
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
        return '%s [%s - %s]' % (self.name, self.central.name, self.central.subgerencia.name)

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

    # Un equipo puede pertenecer a 1 o más unidades
    unidades = models.ManyToManyField(Unidad, verbose_name='Unidades')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['name', ]


# Modelos para Trafo y atributos relacionados
class Trafo(Equipo):
    # Options
    A = '1'
    P = '2'
    ESTATUS_CHOICES = (
        (A, 'Aprobada'),
        (P, 'Pendiente'),
    )

    n_devanados = models.IntegerField(verbose_name='Número de Devanados')
    kv_nominal_at = models.FloatField(verbose_name='KV Nominal AT')
    kv_nominal_bt = models.FloatField(verbose_name='KV Nominal BT')
    elevacion_temperatura = models.FloatField(verbose_name='Elevación de Temperatura')
    estatus_revision = models.CharField(verbose_name='Estatus de Revisión', choices=ESTATUS_CHOICES, default=P)
    fecha_revision_aprobada = models.DateField(verbose_name='Fecha de Revisión Aprobada', blank=True, null=True)
    tipo_servicio = models.ForeignKey('TipoServicio', on_delete=models.CASCADE, verbose_name='Tipo de Servicio')
    configuracion = models.ForeignKey('Configuracion', on_delete=models.CASCADE, verbose_name='Configuración')
    fase = models.ForeignKey('Fase', on_delete=models.CASCADE, verbose_name='Fase')
    conexion = models.ForeignKey('Conexion', on_delete=models.CASCADE, verbose_name='Conexión')
    enfriamiento = models.ForeignKey('Enfriamiento', on_delete=models.CASCADE, verbose_name='Enfriamiento')
    mva = models.ForeignKey('MVA', on_delete=models.CASCADE, verbose_name='MVA')
    tension = models.ForeignKey('Tension', on_delete=models.CASCADE, verbose_name='Tensión kV')
    impedancia = models.ForeignKey('Impedancia', on_delete=models.CASCADE, verbose_name='Impedancia')
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, verbose_name='Marca')

    def __str__(self):
        unidades_ = ", ".join([unidad.name for unidad in self.unidades.all()])
        central_ = self.unidades.first().central.name
        subgerencia_ = self.unidades.first().central.subgerencia.name
        eps_ = self.unidades.first().central.subgerencia.eps.name
        return '%s [%s] - [%s] - [%s] - [%s]' % (self.name, unidades_, central_, subgerencia_, eps_)

    class Meta:
        verbose_name = 'Trafo'
        verbose_name_plural = 'Trafos'
        ordering = ['name', ]


class Accesorio(models.Model):
    instalado = models.BooleanField(verbose_name='Instalado', default=False)
    en_servicio = models.BooleanField(verbose_name='En Servicio', default=False)
    razon_fuera_servicio = models.TextField(verbose_name='Razón Fuera de Servicio', blank=True)
    tipo_accesorio = models.ForeignKey('TipoAccesorio', on_delete=models.CASCADE, verbose_name='Tipo de Accesorio')
    trafo = models.ForeignKey(Trafo, related_name='accesorios', on_delete=models.CASCADE, verbose_name='Trafo')

    def __str__(self):
        return self.tipo_accesorio.name

    class Meta:
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorios'
        ordering = ['tipo_accesorio', ]

    @property
    def get_trafo(self):
        return self.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.trafo.unidades.all()])


class TipoAccesorio(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Accesorio'
        verbose_name_plural = 'Tipos de Accesorios'
        ordering = ['name', ]


class TipoServicio(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Servicio'
        verbose_name_plural = 'Tipos de Servicio'
        ordering = ['name', ]


class Configuracion(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Configuración'
        verbose_name_plural = 'Configuraciones'
        ordering = ['name', ]


class Fase(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fase'
        verbose_name_plural = 'Fases'
        ordering = ['name', ]


class Conexion(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Conexión'
        verbose_name_plural = 'Conexiones'
        ordering = ['name', ]


class Enfriamiento(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Enfriamiento'
        verbose_name_plural = 'Enfriamientos'
        ordering = ['name', ]


class MVA(models.Model):
    mva_1 = models.FloatField(verbose_name='MVA 1', default=0)
    mva_2 = models.FloatField(verbose_name='MVA 2', default=0)
    mva_3 = models.FloatField(verbose_name='MVA 3', default=0)
    mva_4 = models.FloatField(verbose_name='MVA 4', default=0)

    def __str__(self):
        return '%s / %s / %s / %s ' % (self.mva_1, self.mva_2, self.mva_3, self.mva_4)

    class Meta:
        verbose_name = 'MVA'
        verbose_name_plural = 'MVA'


class Tension(models.Model):
    tension_1 = models.FloatField(verbose_name='Tensión 1', default=0)
    tension_2 = models.FloatField(verbose_name='Tensión 2', default=0)
    tension_3 = models.FloatField(verbose_name='Tensión 3', default=0)

    def __str__(self):
        return '%s / %s / %s' % (self.tension_1, self.tension_2, self.tension_3)

    class Meta:
        verbose_name = 'Tensión'
        verbose_name_plural = 'Tensiones'


class Impedancia(models.Model):
    z_1 = models.FloatField(verbose_name='Z 1', default=0)
    z_2 = models.FloatField(verbose_name='Z 2', default=0)
    z_3 = models.FloatField(verbose_name='Z 3', default=0)
    z_4 = models.FloatField(verbose_name='Z 4', default=0)

    def __str__(self):
        return '%s / %s / %s / %s ' % (self.z_1, self.z_2, self.z_3, self.z_4)

    class Meta:
        verbose_name = 'Impedancia'
        verbose_name_plural = 'Impedancias'


class Marca(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name', ]


# Modelos para Generador y atributos relacionados
# class Generador(Equipo):
#     pass
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Generador'
#         verbose_name_plural = 'Generadores'
#         ordering = ['name', ]


# Modelos para Pruebas
class Prueba(models.Model):
    matricula = models.CharField(max_length=50, verbose_name='Matrícula', unique=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    trafo = models.ForeignKey(Trafo, on_delete=models.CASCADE, verbose_name='Trafo')

    def __str__(self):
        return self.matricula

    class Meta:
        verbose_name = 'Prueba'
        verbose_name_plural = 'Pruebas'
        ordering = ['matricula', ]

    @property
    def get_trafo(self):
        return self.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.trafo.unidades.all()])

    @property
    def get_central(self):
        return self.trafo.unidades.first().central.name

    @property
    def get_subgerencia(self):
        return self.trafo.unidades.first().central.subgerencia.name

    @property
    def get_eps(self):
        return self.trafo.unidades.first().central.subgerencia.eps.name


# Prueba Eléctrica de Trafos y atributos relacionados
class ElectricaTrafo(models.Model):
    fecha_prueba = models.DateField(verbose_name='Fecha de Prueba')
    procesado_por = models.CharField(max_length=255, verbose_name='Procesado por', unique=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, verbose_name='Prueba')

    def __str__(self):
        return self.prueba.matricula

    class Meta:
        verbose_name = 'Prueba Eléctrica de Trafos'
        verbose_name_plural = 'Pruebas Eléctricas de Trafos'
        ordering = ['fecha_prueba', 'prueba__matricula', ]

    @property
    def get_prueba(self):
        return self.prueba.matricula

    @property
    def get_trafo(self):
        return self.prueba.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.prueba.trafo.unidades.all()])

    @property
    def get_central(self):
        return self.prueba.trafo.unidades.first().central.name

    @property
    def get_subgerencia(self):
        return self.prueba.trafo.unidades.first().central.subgerencia.name

    @property
    def get_eps(self):
        return self.prueba.trafo.unidades.first().central.subgerencia.eps.name


# Prueba Eléctrica de Trafos - Respuesta de Frecuencia
class RespuestaFrecuencia(models.Model):
    zona_1 = models.FloatField(verbose_name='Zona 1')
    zona_2 = models.FloatField(verbose_name='Zona 2')
    zona_3 = models.FloatField(verbose_name='Zona 3')
    zona_4 = models.FloatField(verbose_name='Zona 4')
    comentarios = models.TextField(verbose_name='Comentarios', blank=True)
    diferencia_realizacion_prueba = models.FloatField(verbose_name='Diferencia de Realización de Prueba', blank=True, null=True)
    respuesta_frecuencia_dielectrica = models.FloatField(verbose_name='Respuesta de Frecuencia Dieléctrica', blank=True, null=True)

    electrica_trafo = models.ForeignKey(ElectricaTrafo, on_delete=models.CASCADE, verbose_name='Prueba Eléctrica de Trafos')

    def __str__(self):
        return 'Zona 1: %s, Zona 2: %s, Zona 3: %s, Zona 4: %s' % (self.zona_1, self.zona_2, self.zona_3, self.zona_4)

    class Meta:
        verbose_name = 'Respuesta de Frecuencia'
        verbose_name_plural = 'Respuestas de Frecuencia'

    @property
    def get_matricula(self):
        return self.electrica_trafo.prueba.matricula


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento
class ResistenciaAislamiento(models.Model):
    r_a_30_seg = models.FloatField(verbose_name='Resistencia de Aislamiento a 30 seg')
    r_a_1_min = models.FloatField(verbose_name='Resistencia de Aislamiento a 1 min')
    r_a_10_min = models.FloatField(verbose_name='Resistencia de Aislamiento a 10 min')
    temperatura_prueba = models.FloatField(verbose_name='Temperatura de Prueba')
    factor_k = models.FloatField(verbose_name='Factor K', blank=True, null=True)
    indice_absorcion = models.FloatField(verbose_name='Índice de Absorción', blank=True, null=True)
    indice_polarizacion = models.FloatField(verbose_name='Índice de Polarización', blank=True, null=True)

    electrica_trafo = models.ForeignKey(ElectricaTrafo, on_delete=models.CASCADE, verbose_name='Prueba Eléctrica de Trafos')

    class Meta:
        verbose_name = 'Resistencia de Aislamiento'
        verbose_name_plural = 'Resistencias de Aislamiento'

    @property
    def get_matricula(self):
        return self.electrica_trafo.prueba.matricula


# Función que permite calcular valores para factor_k, indice_polarizacion e indice_absorcion
# @receiver(models.signals.pre_save, sender=ResistenciaAislamiento)
# def calculate_values(sender, instance, **kwargs):
#     # Calcula el valor de factor_k
#     instance.factor_k = math.pow(0.5, (40.00 - instance.temperatura_prueba) / 10)
#
#     # Calcula el valor de indice_absorcion
#     instance.indice_absorcion = None if instance.r_a_30_seg == 0 else instance.r_a_1_min / instance.r_a_30_seg
#
#     # Calcula el valor de indice_polarizacion
#     instance.indice_polarizacion = None if instance.r_a_1_min == 0 else instance.r_a_10_min / instance.r_a_1_min


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento - CH
class ResistenciaAislamientoCH(ResistenciaAislamiento):
    # No hay atributos adicionales

    class Meta:
        verbose_name = 'Resistencia de Aislamiento - CH'
        verbose_name_plural = 'Resistencias de Aislamiento - CH'

    @property
    def get_matricula(self):
        return self.electrica_trafo.prueba.matricula


# Función que permite calcular valores para factor_k, indice_polarizacion e indice_absorcion
@receiver(models.signals.pre_save, sender=ResistenciaAislamientoCH)
def calculate_values(sender, instance, **kwargs):
    # Calcula el valor de factor_k
    instance.factor_k = math.pow(0.5, (40.00 - instance.temperatura_prueba) / 10)

    # Calcula el valor de indice_absorcion
    instance.indice_absorcion = None if instance.r_a_30_seg == 0 else instance.r_a_1_min / instance.r_a_30_seg

    # Calcula el valor de indice_polarizacion
    instance.indice_polarizacion = None if instance.r_a_1_min == 0 else instance.r_a_10_min / instance.r_a_1_min


# Prueba Eléctrica de Trafos - Factor de Potencia


# Prueba Eléctrica de Trafos - Capacitancia


# Prueba Eléctrica de Trafos - TTR


# Prueba Eléctrica de Trafos - Placa Boquilla


# Prueba Eléctrica de Trafos - Factor de Potencia Boquilla


# Prueba Eléctrica de Trafos - Resistencia Devanado AT


# Prueba Eléctrica de Trafos - Resistencia Devanado BT


# Prueba Cromatografía de gases y atributos relacionados
class EstatusPrueba(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estatus de Prueba'
        verbose_name_plural = 'Estatus de Pruebas'
        ordering = ['name', ]


class CromatografiaGases(models.Model):
    estatus_prueba = models.ForeignKey(EstatusPrueba, on_delete=models.CASCADE, verbose_name='Estatus de Prueba')
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, verbose_name='Prueba')

    def __str__(self):
        return self.prueba.matricula

    class Meta:
        verbose_name = 'Cromatografía de Gases'
        verbose_name_plural = 'Cromatografías de Gases'
        ordering = ['prueba__matricula', ]

    @property
    def get_prueba(self):
        return self.prueba.matricula

    @property
    def get_trafo(self):
        return self.prueba.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.prueba.trafo.unidades.all()])

    @property
    def get_central(self):
        return self.prueba.trafo.unidades.first().central.name

    @property
    def get_subgerencia(self):
        return self.prueba.trafo.unidades.first().central.subgerencia.name

    @property
    def get_eps(self):
        return self.prueba.trafo.unidades.first().central.subgerencia.eps.name


class CromatografiaGasesRelacionO2N2(models.Model):
    edad = models.FloatField(verbose_name='Edad', null=True, blank=True)
    o2 = models.FloatField(verbose_name='O2', null=True, blank=True)
    n2 = models.FloatField(verbose_name='N2', null=True, blank=True)
    o2entren2 = models.FloatField(verbose_name='O2 entre N2', null=True, blank=True)
    h2 = models.FloatField(verbose_name='H2', null=True, blank=True)
    ch4 = models.FloatField(verbose_name='CH4', null=True, blank=True)
    co = models.FloatField(verbose_name='CO', null=True, blank=True)
    c2h6 = models.FloatField(verbose_name='C2H6', null=True, blank=True)
    co2 = models.FloatField(verbose_name='CO2', null=True, blank=True)
    c2h4 = models.FloatField(verbose_name='C2H4', null=True, blank=True)
    c2h2 = models.FloatField(verbose_name='C2H2', null=True, blank=True)
    total_gc = models.FloatField(verbose_name='Total GC', null=True, blank=True)
    p_incremento = models.FloatField(verbose_name='% Incremento', null=True, blank=True)
    p_tgc_referencia = models.FloatField(verbose_name='% TGC Referencia', null=True, blank=True)
    p_tgc_ultimo = models.FloatField(verbose_name='% TGC Último', null=True, blank=True)
    diferencial = models.FloatField(verbose_name='Diferencial', null=True, blank=True)
    absoluto = models.FloatField(verbose_name='Absoluto', null=True, blank=True)
    cromatografia_gases = models.ForeignKey(CromatografiaGases, on_delete=models.CASCADE, verbose_name='Cromatografía de Gases')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    def __str__(self):
        return self.cromatografia_gases.prueba.matricula

    class Meta:
        verbose_name = 'Relación O2/N2'
        verbose_name_plural = 'Relaciones O2/N2'
        ordering = ['cromatografia_gases__prueba__matricula', ]

    @property
    def get_prueba(self):
        return self.cromatografia_gases.prueba.matricula

    @property
    def get_status(self):
        return self.cromatografia_gases.estatus_prueba.name

    @property
    def get_trafo(self):
        return self.cromatografia_gases.prueba.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.cromatografia_gases.prueba.trafo.unidades.all()])

    @property
    def get_central(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.name

    @property
    def get_subgerencia(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.subgerencia.name

    @property
    def get_eps(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.subgerencia.eps.name


class DiferencialO2N2(models.Model):
    h2 = models.FloatField(verbose_name='H2', null=True, blank=True)
    ch4 = models.FloatField(verbose_name='CH4', null=True, blank=True)
    co = models.FloatField(verbose_name='CO', null=True, blank=True)
    c2h6 = models.FloatField(verbose_name='C2H6', null=True, blank=True)
    co2 = models.FloatField(verbose_name='CO2', null=True, blank=True)
    c2h4 = models.FloatField(verbose_name='C2H4', null=True, blank=True)
    c2h2 = models.FloatField(verbose_name='C2H2', null=True, blank=True)
    cromatografia_gases = models.ForeignKey(CromatografiaGases, on_delete=models.CASCADE, verbose_name='Cromatografía de Gases')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    def __str__(self):
        return self.cromatografia_gases.prueba.matricula

    class Meta:
        verbose_name = 'Diferencial O2/N2'
        verbose_name_plural = 'Diferenciales O2/N2'
        ordering = ['cromatografia_gases__prueba__matricula', ]

    @property
    def get_prueba(self):
        return self.cromatografia_gases.prueba.matricula

    @property
    def get_status(self):
        return self.cromatografia_gases.estatus_prueba.name

    @property
    def get_trafo(self):
        return self.cromatografia_gases.prueba.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.cromatografia_gases.prueba.trafo.unidades.all()])

    @property
    def get_central(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.name

    @property
    def get_subgerencia(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.subgerencia.name

    @property
    def get_eps(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.subgerencia.eps.name


class VelocidadEntrePruebas(models.Model):
    meses_entre_pruebas = models.FloatField(verbose_name='Meses entre Pruebas', null=True, blank=True)
    h2 = models.FloatField(verbose_name='H2', null=True, blank=True)
    ch4 = models.FloatField(verbose_name='CH4', null=True, blank=True)
    co = models.FloatField(verbose_name='CO', null=True, blank=True)
    c2h6 = models.FloatField(verbose_name='C2H6', null=True, blank=True)
    co2 = models.FloatField(verbose_name='CO2', null=True, blank=True)
    c2h4 = models.FloatField(verbose_name='C2H4', null=True, blank=True)
    c2h2 = models.FloatField(verbose_name='C2H2', null=True, blank=True)
    cromatografia_gases = models.ForeignKey(CromatografiaGases, on_delete=models.CASCADE, verbose_name='Cromatografía de Gases')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    def __str__(self):
        return self.cromatografia_gases.prueba.matricula

    class Meta:
        verbose_name = 'Velocidad entre Pruebas'
        verbose_name_plural = 'Velocidades entre Pruebas'
        ordering = ['cromatografia_gases__prueba__matricula', ]

    @property
    def get_prueba(self):
        return self.cromatografia_gases.prueba.matricula

    @property
    def get_status(self):
        return self.cromatografia_gases.estatus_prueba.name

    @property
    def get_trafo(self):
        return self.cromatografia_gases.prueba.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.cromatografia_gases.prueba.trafo.unidades.all()])

    @property
    def get_central(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.name

    @property
    def get_subgerencia(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.subgerencia.name

    @property
    def get_eps(self):
        return self.cromatografia_gases.prueba.trafo.unidades.first().central.subgerencia.eps.name


# Prueba Físico Químicas y atributos relacionados
class FisicoQuimica(models.Model):
    fecha_prueba = models.DateField(verbose_name='Fecha de Prueba')
    exploratoria_aceite = models.FloatField(verbose_name='Prueba Exploratoria de Aceite')
    analisis_gases_disueltos = models.FloatField(verbose_name='Análisis de Gases Disueltos')
    contenido_humedad = models.FloatField(verbose_name='Contenido de Humedad')
    fp_liquido_25c = models.FloatField(verbose_name='FP Líquido a 25°C')
    fp_liquido_100c = models.FloatField(verbose_name='PF Líquido a 100°C')
    contenido_inhibidor_oxidacion = models.FloatField(verbose_name='Contenido de Inhibidor de Oxidación')
    compuestos_furanicos = models.FloatField(verbose_name='Compuestos Furánicos')
    rigidez_dielectrica = models.FloatField(verbose_name='Rigidez Dieléctrica')
    factor_potencia = models.FloatField(verbose_name='Factor de Potencia')
    tension_interfacial = models.FloatField(verbose_name='Tensión Interfacial')
    color = models.FloatField(verbose_name='Color')
    examinacion_visual = models.TextField(verbose_name='Examinación Visual', blank=True)
    nivel_neutralizacion = models.FloatField(verbose_name='Nivel de Neutralización')
    contenido_agua = models.FloatField(verbose_name='Contenido de Agua')
    contenido_inhibidor_oxidacion_especifico = models.FloatField(verbose_name='Contenido de Inhibidor de Oxidación Específico')
    azufre_corrosivo = models.FloatField(verbose_name='Azufre Corrosivo')
    humedad_resiudal = models.FloatField(verbose_name='Humedad Residual')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modify = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, verbose_name='Prueba')

    def __str__(self):
        return self.prueba.matricula

    class Meta:
        verbose_name = 'Prueba Físico Química'
        verbose_name_plural = 'Pruebas Físico Químicas'
        ordering = ['fecha_prueba', 'prueba__matricula', 'prueba__trafo', 'prueba__trafo__unidades', 'prueba__trafo__unidades__central', ]

    @property
    def get_prueba(self):
        return self.prueba.matricula

    @property
    def get_trafo(self):
        return self.prueba.trafo.name

    @property
    def get_unidades(self):
        return ", ".join([unidad.name for unidad in self.prueba.trafo.unidades.all()])

    @property
    def get_central(self):
        return self.prueba.trafo.unidades.first().central.name

    @property
    def get_subgerencia(self):
        return self.prueba.trafo.unidades.first().central.subgerencia.name

    @property
    def get_eps(self):
        return self.prueba.trafo.unidades.first().central.subgerencia.eps.name

