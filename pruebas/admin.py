from django.contrib import admin
from .models import *
from django.http import HttpResponse


class AdminEPS(admin.ModelAdmin):
    list_display = ['name', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = EPS


class AdminSubgerencia(admin.ModelAdmin):
    list_display = ['name', 'eps', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'eps__name', ]
    ordering = ['name', ]

    class Meta:
        model = Subgerencia


class AdminCentral(admin.ModelAdmin):
    list_display = ['alias', 'name', 'subgerencia', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['alias', 'name', 'subgerencia__name', ]
    ordering = ['name', ]

    class Meta:
        model = Central


class AdminUnidad(admin.ModelAdmin):
    list_display = ['name', 'central', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'central__name', ]
    ordering = ['name', ]

    class Meta:
        model = Unidad


class AdminEquipo(admin.ModelAdmin):
    def get_unidades_names(self, obj):
        return ', '.join([unidad.name for unidad in obj.unidades.all()])

    get_unidades_names.short_description = 'Unidades'

    list_display = ['name', 'n_serie', 'ano_puesta_servicio', 'condicion_operacion', 'razon_fuera_servicio',
                    'problematica_operativa', 'indice_condicion', 'observaciones', 'get_unidades_names', 'create',
                    'modify', ]
    filter_horizontal = ('unidades',)
    list_filter = ['create', 'modify', ]
    search_fields = ['alias', 'name', 'unidad__name', ]
    ordering = ['name', ]

    class Meta:
        model = Equipo

    def display_unidades(self, obj):
        return ", ".join([unidad.nombre for unidad in obj.unidades.all()])


class AdminTrafo(admin.ModelAdmin):
    list_display = ['name', 'n_serie', 'ano_puesta_servicio', 'condicion_operacion', 'razon_fuera_servicio',
                    'problematica_operativa', 'indice_condicion', 'observaciones', 'n_devanados', 'kv_nominal_at',
                    'kv_nominal_bt', 'tension_kv', 'elevacion_temperatura', 'tipo_servicio', 'configuracion', 'fase',
                    'conexion', 'enfriamiento', 'mva', 'impedancia', 'marca', 'estatus_revision',
                    'fecha_revision_aprobada', 'create', 'modify', ]
    filter_horizontal = ('unidades', )
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'unidad__name', ]
    ordering = ['name', ]

    class Meta:
        model = Trafo

    def display_unidades(self, obj):
        return ", ".join([unidad.nombre for unidad in obj.unidades.all()])


class AdminTipoServicio(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = TipoServicio


class AdminConfiguracion(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Configuracion


class AdminFase(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Fase


class AdminConexion(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Conexion


class AdminEnfriamiento(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Enfriamiento


class AdminMVA(admin.ModelAdmin):
    list_display = ['mva_1', 'mva_2', 'mva_3', 'mva_4', ]

    class Meta:
        model = MVA


class AdminImpedancia(admin.ModelAdmin):
    list_display = ['z_1', 'z_2', 'z_3', 'z_4', ]

    class Meta:
        model = Impedancia


class AdminMarca(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Marca


class AdminPrueba(admin.ModelAdmin):
    list_display = ['matricula', 'trafo', 'get_unidades', 'get_central', 'get_subgerencia', 'get_eps', 'create',
                    'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['matricula', ]
    ordering = ['matricula', ]

    class Meta:
        model = Prueba


class AdminElectricaTrafo(admin.ModelAdmin):
    list_display = ['prueba', 'fecha_prueba', 'procesado_por', 'get_trafo', 'get_unidades', 'get_central',
                    'get_subgerencia', 'get_eps', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['prueba__matricula', ]
    ordering = ['prueba__matricula', ]

    class Meta:
        model = ElectricaTrafo


# class AdminRespuestaFrecuencia(admin.ModelAdmin):
#     list_display = ['matricula', 'zona_1', 'zona_2', 'zona_3', 'zona_4', ]
#     search_fields = ['electrica_trafo__prueba__matricula', ]
#     ordering = ['electrica_trafo__prueba__matricula', ]
#
#     def matricula(self, obj):
#         return obj.prueba.matricula
#
#     class Meta:
#         model = RespuestaFrecuencia


class AdminFisicoQuimica(admin.ModelAdmin):
    list_display = ['prueba', 'fecha_prueba', 'exploratoria_aceite', 'analisis_gases_disueltos', 'contenido_humedad',
                    'fp_liquido_25c', 'fp_liquido_100c', 'contenido_inhibidor_oxidacion', 'compuestos_furanicos',
                    'rigidez_dielectrica', 'factor_potencia', 'tension_interfacial', 'color', 'examinacion_visual',
                    'nivel_neutralizacion', 'contenido_agua', 'contenido_inhibidor_oxidacion_especifico',
                    'azufre_corrosivo', 'humedad_resiudal', 'get_trafo', 'get_unidades', 'get_central',
                    'get_subgerencia', 'get_eps', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['prueba__matricula', ]
    ordering = ['prueba__matricula', ]

    class Meta:
        model = FisicoQuimica


admin.site.register(EPS, AdminEPS)
admin.site.register(Subgerencia, AdminSubgerencia)
admin.site.register(Central, AdminCentral)
admin.site.register(Unidad, AdminUnidad)
admin.site.register(Equipo, AdminEquipo)
admin.site.register(Trafo, AdminTrafo)
admin.site.register(TipoServicio, AdminTipoServicio)
admin.site.register(Configuracion, AdminConfiguracion)
admin.site.register(Fase, AdminFase)
admin.site.register(Conexion, AdminConexion)
admin.site.register(Enfriamiento, AdminEnfriamiento)
admin.site.register(MVA, AdminMVA)
admin.site.register(Impedancia, AdminImpedancia)
admin.site.register(Marca, AdminMarca)
admin.site.register(Prueba, AdminPrueba)
admin.site.register(ElectricaTrafo, AdminElectricaTrafo)
# admin.site.register(RespuestaFrecuencia, AdminRespuestaFrecuencia)
admin.site.register(FisicoQuimica, AdminFisicoQuimica)
