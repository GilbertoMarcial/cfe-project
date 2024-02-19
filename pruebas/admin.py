from django.contrib import admin
from .models import *
from django.http import HttpResponse


# EPS, Subgerencia, Central, Unidad y Equipo
class AdminEPS(admin.ModelAdmin):
    list_display = ['name', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = EPS


admin.site.register(EPS, AdminEPS)


class AdminSubgerencia(admin.ModelAdmin):
    list_display = ['name', 'eps', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'eps__name', ]
    ordering = ['name', ]

    class Meta:
        model = Subgerencia


admin.site.register(Subgerencia, AdminSubgerencia)


class AdminCentral(admin.ModelAdmin):
    list_display = ['alias', 'name', 'subgerencia', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['alias', 'name', 'subgerencia__name', ]
    ordering = ['name', ]

    class Meta:
        model = Central


admin.site.register(Central, AdminCentral)


class AdminUnidad(admin.ModelAdmin):
    list_display = ['name', 'central', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'central__name', ]
    ordering = ['name', ]

    class Meta:
        model = Unidad


admin.site.register(Unidad, AdminUnidad)


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


admin.site.register(Equipo, AdminEquipo)


# Modelos para Trafo y atributos relacionados
class AccesorioInline(admin.TabularInline):
    model = Accesorio
    extra = 1


class AdminTrafo(admin.ModelAdmin):
    def accesorio_1(self, obj):
        return ', '.join(
            [
                obj.accesorios.all()[0].tipo_accesorio.name,
                'Instalado' if obj.accesorios.all()[0].instalado else 'No Instalado',
                'En servicio ' if obj.accesorios.all()[0].en_servicio else 'Fuera de Servicio',
                'Razón fuera de servicio: ' + obj.accesorios.all()[0].razon_fuera_servicio,
            ]
        )

    accesorio_1.short_description = 'Accesorio 1'

    def accesorio_2(self, obj):
        return ', '.join(
            [
                obj.accesorios.all()[1].tipo_accesorio.name,
                'Instalado' if obj.accesorios.all()[1].instalado else 'No Instalado',
                'En servicio ' if obj.accesorios.all()[1].en_servicio else 'Fuera de Servicio',
                'Razón fuera de servicio: ' + obj.accesorios.all()[1].razon_fuera_servicio,
            ]
        )

    accesorio_2.short_description = 'Accesorio 2'

    def accesorio_3(self, obj):
        return ', '.join(
            [
                obj.accesorios.all()[2].tipo_accesorio.name,
                'Instalado' if obj.accesorios.all()[2].instalado else 'No Instalado',
                'En servicio ' if obj.accesorios.all()[2].en_servicio else 'Fuera de Servicio',
                'Razón fuera de servicio: ' + obj.accesorios.all()[2].razon_fuera_servicio,
            ]
        )

    accesorio_3.short_description = 'Accesorio 3'

    list_display = ['name', 'get_unidades', 'get_central', 'get_subgerencia', 'get_eps', 'n_serie',
                    'ano_puesta_servicio', 'condicion_operacion', 'razon_fuera_servicio', 'problematica_operativa',
                    'indice_condicion', 'observaciones', 'n_devanados', 'kv_nominal_at', 'kv_nominal_bt',
                    'elevacion_temperatura', 'tipo_servicio', 'configuracion', 'fase', 'conexion', 'enfriamiento',
                    'mva', 'tension', 'impedancia', 'marca', 'accesorio_1', 'accesorio_2', 'accesorio_3',
                    'estatus_revision', 'fecha_revision_aprobada', 'create', 'modify', ]
    filter_horizontal = ('unidades', )
    list_filter = ['create', 'modify', ]
    search_fields = ['name', 'unidad__name', ]
    inlines = [AccesorioInline, ]
    ordering = ['name', ]

    class Meta:
        model = Trafo


admin.site.register(Trafo, AdminTrafo)


class AdminAccesorio(admin.ModelAdmin):
    list_display = ['instalado', 'en_servicio', 'razon_fuera_servicio', 'tipo_accesorio', 'trafo', 'get_unidades', ]
    search_fields = ['trafo', ]
    ordering = ['trafo', ]

    class Meta:
        model = Accesorio


admin.site.register(Accesorio, AdminAccesorio)


class AdminTipoAccesorio(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = TipoAccesorio


admin.site.register(TipoAccesorio, AdminTipoAccesorio)


class AdminTipoServicio(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = TipoServicio


admin.site.register(TipoServicio, AdminTipoServicio)


class AdminConfiguracion(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Configuracion


admin.site.register(Configuracion, AdminConfiguracion)


class AdminFase(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Fase


admin.site.register(Fase, AdminFase)


class AdminConexion(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Conexion


admin.site.register(Conexion, AdminConexion)


class AdminEnfriamiento(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Enfriamiento


admin.site.register(Enfriamiento, AdminEnfriamiento)


class AdminMVA(admin.ModelAdmin):
    list_display = ['mva_1', 'mva_2', 'mva_3', 'mva_4', ]

    class Meta:
        model = MVA


admin.site.register(MVA, AdminMVA)


class AdminTension(admin.ModelAdmin):
    list_display = ['tension_1', 'tension_2', 'tension_3', ]

    class Meta:
        model = Tension


admin.site.register(Tension, AdminTension)


class AdminImpedancia(admin.ModelAdmin):
    list_display = ['z_1', 'z_2', 'z_3', 'z_4', ]

    class Meta:
        model = Impedancia


admin.site.register(Impedancia, AdminImpedancia)


class AdminMarca(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = Marca


admin.site.register(Marca, AdminMarca)


# Modelos para Pruebas
class AdminPrueba(admin.ModelAdmin):
    list_display = ['matricula', 'trafo', 'get_unidades', 'get_central', 'get_subgerencia', 'get_eps', 'create',
                    'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['matricula', ]
    ordering = ['matricula', ]

    class Meta:
        model = Prueba


admin.site.register(Prueba, AdminPrueba)


# Prueba Eléctrica de Trafos y atributos relacionados
class AdminElectricaTrafo(admin.ModelAdmin):
    list_display = ['prueba', 'fecha_prueba', 'procesado_por', 'get_trafo', 'get_unidades', 'get_central',
                    'get_subgerencia', 'get_eps', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['prueba__matricula', ]
    ordering = ['prueba__matricula', ]

    class Meta:
        model = ElectricaTrafo


admin.site.register(ElectricaTrafo, AdminElectricaTrafo)


# Prueba Eléctrica de Trafos - Respuesta de Frecuencia
class AdminRespuestaFrecuencia(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia', 'get_eps',
                    'get_date', 'zona_1', 'zona_2', 'zona_3', 'zona_4', 'comentarios', 'diferencia_realizacion_prueba',
                    'respuesta_frecuencia_dielectrica', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = RespuestaFrecuencia


admin.site.register(RespuestaFrecuencia, AdminRespuestaFrecuencia)


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento
class AdminResistenciaAislamiento(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'r_a_30_seg', 'r_a_1_min', 'r_a_10_min', 'temperatura_prueba',
                    'factor_k', 'indice_absorcion', 'indice_polarizacion', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = ResistenciaAislamiento


admin.site.register(ResistenciaAislamiento, AdminResistenciaAislamiento)


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento - CH
class AdminResistenciaAislamientoCH(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'r_a_30_seg', 'r_a_1_min', 'r_a_10_min', 'temperatura_prueba', 'factor_k',
                    'indice_absorcion', 'indice_polarizacion', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = ResistenciaAislamientoCH


admin.site.register(ResistenciaAislamientoCH, AdminResistenciaAislamientoCH)


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento - CHL
class AdminResistenciaAislamientoCHL(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'r_a_30_seg', 'r_a_1_min', 'r_a_10_min', 'temperatura_prueba', 'factor_k',
                    'indice_absorcion', 'indice_polarizacion', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = ResistenciaAislamientoCHL


admin.site.register(ResistenciaAislamientoCHL, AdminResistenciaAislamientoCHL)


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento - CL
class AdminResistenciaAislamientoCL(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'r_a_30_seg', 'r_a_1_min', 'r_a_10_min', 'temperatura_prueba', 'factor_k',
                    'indice_absorcion', 'indice_polarizacion', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = ResistenciaAislamientoCL


admin.site.register(ResistenciaAislamientoCL, AdminResistenciaAislamientoCL)


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento - CHT
class AdminResistenciaAislamientoCHT(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'r_a_30_seg', 'r_a_1_min', 'r_a_10_min', 'temperatura_prueba', 'factor_k',
                    'indice_absorcion', 'indice_polarizacion', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = ResistenciaAislamientoCHT


admin.site.register(ResistenciaAislamientoCHT, AdminResistenciaAislamientoCHT)


# Prueba Eléctrica de Trafos - Resistencia de Aislamiento - CT
class AdminResistenciaAislamientoCT(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'r_a_30_seg', 'r_a_1_min', 'r_a_10_min', 'temperatura_prueba', 'factor_k',
                    'indice_absorcion', 'indice_polarizacion', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = ResistenciaAislamientoCT


admin.site.register(ResistenciaAislamientoCT, AdminResistenciaAislamientoCT)


# Prueba Cromatografía de gases y atributos relacionados
class AdminEstatusPrueba(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]

    class Meta:
        model = EstatusPrueba


admin.site.register(EstatusPrueba, AdminEstatusPrueba)


class AdminCromatografiaGases(admin.ModelAdmin):
    list_display = ['prueba', 'estatus_prueba', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', ]
    search_fields = ['prueba__matricula', ]
    ordering = ['prueba__matricula', ]

    class Meta:
        model = CromatografiaGases


admin.site.register(CromatografiaGases, AdminCromatografiaGases)


class AdminCromatografiaGasesRelacionO2N2(admin.ModelAdmin):
    list_display = ['cromatografia_gases', 'get_status', 'edad', 'o2', 'n2', 'o2entren2', 'h2', 'ch4', 'co', 'c2h6',
                    'co2', 'c2h4', 'c2h2', 'total_gc', 'p_incremento', 'p_tgc_referencia', 'p_tgc_ultimo',
                    'diferencial', 'absoluto', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['cromatografia_gases__prueba__matricula', ]
    ordering = ['cromatografia_gases__prueba__matricula', ]

    class Meta:
        model = CromatografiaGasesRelacionO2N2


admin.site.register(CromatografiaGasesRelacionO2N2, AdminCromatografiaGasesRelacionO2N2)


class AdminDiferencialO2N2(admin.ModelAdmin):
    list_display = ['cromatografia_gases', 'get_status', 'h2', 'ch4', 'co', 'c2h6', 'co2', 'c2h4', 'c2h2', 'create',
                    'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['cromatografia_gases__prueba__matricula', ]
    ordering = ['cromatografia_gases__prueba__matricula', ]

    class Meta:
        model = DiferencialO2N2


admin.site.register(DiferencialO2N2, AdminDiferencialO2N2)


class AdminVelocidadEntrePruebas(admin.ModelAdmin):
    list_display = ['cromatografia_gases', 'get_status', 'meses_entre_pruebas', 'h2', 'ch4', 'co', 'c2h6', 'co2',
                    'c2h4', 'c2h2', 'create', 'modify', ]
    list_filter = ['create', 'modify', ]
    search_fields = ['cromatografia_gases__prueba__matricula', ]
    ordering = ['cromatografia_gases__prueba__matricula', ]

    class Meta:
        model = VelocidadEntrePruebas


admin.site.register(VelocidadEntrePruebas, AdminVelocidadEntrePruebas)


# Prueba Eléctrica de Trafos - Factor de Potencia
# Prueba Eléctrica de Trafos - Factor de Potencia - Tensión Prueba
class AdminDatosFP(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'tension_prueba', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = DatosFP


admin.site.register(DatosFP, AdminDatosFP)


# Prueba Eléctrica de Trafos - Factor de Potencia - CH
class AdminDatosFPCH(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'fp_referencia', 'corriente_ma', 'watts', 'fp', 'p_fp_placa',
                    'velocidad_cambio_fp_placa', 'aceleracion_fp_placa', 'p_fp', 'velocidad_cambio_fp',
                    'aceleracion_fp', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = DatosFPCH


admin.site.register(DatosFPCH, AdminDatosFPCH)


# Prueba Eléctrica de Trafos - Factor de Potencia - CHL
class AdminDatosFPCHL(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'fp_referencia', 'corriente_ma', 'watts', 'fp', 'p_fp_placa',
                    'velocidad_cambio_fp_placa', 'aceleracion_fp_placa', 'p_fp', 'velocidad_cambio_fp',
                    'aceleracion_fp', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = DatosFPCHL


admin.site.register(DatosFPCHL, AdminDatosFPCHL)


# Prueba Eléctrica de Trafos - Factor de Potencia - CL
class AdminDatosFPCL(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'fp_referencia', 'corriente_ma', 'watts', 'fp', 'p_fp_placa',
                    'velocidad_cambio_fp_placa', 'aceleracion_fp_placa', 'p_fp', 'velocidad_cambio_fp',
                    'aceleracion_fp', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = DatosFPCL


admin.site.register(DatosFPCL, AdminDatosFPCL)


# Prueba Eléctrica de Trafos - Factor de Potencia - CHT
class AdminDatosFPCHT(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'fp_referencia', 'corriente_ma', 'watts', 'fp', 'p_fp_placa',
                    'velocidad_cambio_fp_placa', 'aceleracion_fp_placa', 'p_fp', 'velocidad_cambio_fp',
                    'aceleracion_fp', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = DatosFPCHT


admin.site.register(DatosFPCHT, AdminDatosFPCHT)


# Prueba Eléctrica de Trafos - Factor de Potencia - CT
class AdminDatosFPCT(admin.ModelAdmin):
    list_display = ['get_matricula', 'get_date', 'get_trafo', 'get_unidades', 'get_central', 'get_subgerencia',
                    'get_eps', 'fp_referencia', 'corriente_ma', 'watts', 'fp', 'p_fp_placa',
                    'velocidad_cambio_fp_placa', 'aceleracion_fp_placa', 'p_fp', 'velocidad_cambio_fp',
                    'aceleracion_fp', ]
    search_fields = ['electrica_trafo__prueba__matricula', ]
    ordering = ['electrica_trafo__prueba__matricula', ]

    class Meta:
        model = DatosFPCT


admin.site.register(DatosFPCT, AdminDatosFPCT)


# Prueba Físico Químicas y atributos relacionados
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


admin.site.register(FisicoQuimica, AdminFisicoQuimica)
