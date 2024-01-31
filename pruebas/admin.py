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


admin.site.register(EPS, AdminEPS)
admin.site.register(Subgerencia, AdminSubgerencia)
