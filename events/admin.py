from django.contrib import admin

from django.contrib import admin
from .models import Pais, Departamento, Ciudad, Lugar, TipoContratacion, TipoEmpleado, Facultad, Empleado, Area, Programa, Sede, Usuario, Evento, Comentario

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('nombre',)

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'cod_pais')
    search_fields = ('nombre',)
    list_filter = ('cod_pais',)

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'cod_dpto')
    search_fields = ('nombre',)
    list_filter = ('cod_dpto',)

@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad')
    search_fields = ('nombre',)
    list_filter = ('ciudad',)

@admin.register(TipoContratacion)
class TipoContratacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(TipoEmpleado)
class TipoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'ubicacion', 'nro_telefono', 'id_decano')
    search_fields = ('nombre',)
    list_filter = ('ubicacion',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombres', 'apellidos', 'email', 'tipo_contratacion', 'tipo_empleado', 'cod_facultad', 'codigo_sede', 'lugar_nacimiento')
    search_fields = ('nombres', 'apellidos', 'email')
    list_filter = ('tipo_contratacion', 'tipo_empleado', 'cod_facultad', 'codigo_sede')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'codigo_facultad', 'id_coordinador')
    search_fields = ('nombre',)
    list_filter = ('codigo_facultad',)

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'codigo_area')
    search_fields = ('nombre',)
    list_filter = ('codigo_area',)

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'cod_ciudad')
    search_fields = ('nombre',)
    list_filter = ('cod_ciudad',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre_usuario', 'nombre_completo', 'tipo_relacion', 'email', 'ciudad')
    search_fields = ('nombre_usuario', 'nombre_completo', 'email')
    list_filter = ('tipo_relacion', 'ciudad')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'categorias', 'fecha', 'lugar', 'programa_organizador')
    search_fields = ('titulo', 'categorias')
    list_filter = ('fecha', 'lugar', 'programa_organizador')
    filter_horizontal = ('asistentes', 'conferencistas', 'facultades_organizadoras')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('evento', 'usuario', 'texto')
    search_fields = ('evento', 'usuario', 'texto')

