from django.contrib import admin
from .models import Socios, Detalle_Socios, Reuniones, Asistencias, Ingresos, Egresos, Usuarios

# Registro de modelos usando decoradores


@admin.register(Socios)
class SociosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombres', 'apellidos', 'celular', 'correo_electronico', 'fecha_nacimiento')
    search_fields = ('cedula', 'nombres', 'apellidos')
    list_filter = ('fecha_nacimiento',)

@admin.register(Detalle_Socios)
class DetalleSociosAdmin(admin.ModelAdmin):
    list_display = ('socio', 'genero', 'estado_civil', 'cargo', 'estado', 'fecha_ingreso', 'fecha_salida')
    search_fields = ('socio__cedula', 'socio__nombres', 'socio__apellidos')
    list_filter = ('estado', 'cargo', 'genero')

@admin.register(Reuniones)
class ReunionesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fecha', 'lugar', 'tipo', 'Descripcion')
    search_fields = ('codigo', 'lugar', 'Descripcion')
    list_filter = ('fecha', 'tipo')

@admin.register(Asistencias)
class AsistenciasAdmin(admin.ModelAdmin):
    list_display = ('socio', 'reunion', 'estado')
    search_fields = ('socio__cedula', 'reunion__codigo')
    list_filter = ('estado', 'reunion__fecha')

@admin.register(Ingresos)
class IngresosAdmin(admin.ModelAdmin):
    list_display = ('socio', 'tipo', 'descripcion', 'monto', 'fecha')
    search_fields = ('socio__cedula', 'tipo', 'descripcion')
    list_filter = ('tipo', 'fecha')

@admin.register(Egresos)
class EgresosAdmin(admin.ModelAdmin):
    list_display = ('socio', 'tipo', 'descripcion', 'monto', 'fecha')
    search_fields = ('socio__cedula', 'tipo', 'descripcion')
    list_filter = ('tipo', 'fecha')

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'usuarios')
    search_fields = ('cedula', 'usuarios')