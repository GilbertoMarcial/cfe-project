from django.contrib import admin
from .models import *
from django.http import HttpResponse


class AdminEPS(admin.ModelAdmin):
    list_display = ['name', 'create', 'modify', ]
    list_display_links = None
    list_filter = ['create', 'modify', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = EPS


class AdminSubgerencia(admin.ModelAdmin):
    list_display = ['name', 'eps', 'create', 'modify', ]
    list_display_links = None
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'eps__name', ]
    ordering = ['name', ]

    class Meta:
        model = Subgerencia


class AdminCentral(admin.ModelAdmin):
    list_display = ['alias', 'name', 'subgerencia', 'create', 'modify', ]
    list_display_links = None
    list_filter = ['create', 'modify', ]
    search_fields = ['alias', 'name', 'subgerencia__name', ]
    ordering = ['name', ]

    class Meta:
        model = Central


class AdminUnidad(admin.ModelAdmin):
    list_display = ['name', 'central', 'create', 'modify', ]
    list_display_links = None
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'central__name', ]
    ordering = ['name', ]

    class Meta:
        model = Unidad


class AdminEquipo(admin.ModelAdmin):
    def get_unidades_names(self, obj):
        return ', '.join([unidad.name for unidad in obj.unidades.all()])

    get_unidades_names.short_description = 'Unidades'

    list_display = ['name', 'n_serie', 'ano_puesta_servicio', 'condicion_operacion', 'razon_fuera_servicio', 'problematica_operativa', 'indice_condicion', 'observaciones', 'get_unidades_names', 'create', 'modify', ]
    filter_horizontal = ('unidades',)
    list_display_links = None
    list_filter = ['create', 'modify', ]
    search_fields = ['alias', 'name', 'unidad__name', ]
    ordering = ['name', ]

    class Meta:
        model = Equipo

    def display_unidades(self, obj):
        return ", ".join([unidad.nombre for unidad in obj.unidades.all()])


class AdminTrafo(admin.ModelAdmin):
    list_display = ['name', 'n_serie', 'ano_puesta_servicio', 'condicion_operacion', 'razon_fuera_servicio', 'problematica_operativa', 'indice_condicion', 'observaciones', 'n_devanados', 'kv_nominal_at', 'kv_nominal_bt', 'tension_kv', 'elevacion_temperatura', 'create', 'modify', ]
    filter_horizontal = ('unidades',)
    list_display_links = None
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'unidad__name', ]
    ordering = ['name', ]

    class Meta:
        model = Trafo

    def display_unidades(self, obj):
        return ", ".join([unidad.nombre for unidad in obj.unidades.all()])


admin.site.register(EPS, AdminEPS)
admin.site.register(Subgerencia, AdminSubgerencia)
admin.site.register(Central, AdminCentral)
admin.site.register(Unidad, AdminUnidad)
admin.site.register(Equipo, AdminEquipo)
admin.site.register(Trafo, AdminTrafo)
