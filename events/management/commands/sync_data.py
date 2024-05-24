from django.core.management.base import BaseCommand
from events.models import Empleado, Facultad, Area, Programa, Sede, Pais, Departamento, Ciudad, Lugar, Usuario, Evento, Comentario, TipoContratacion, TipoEmpleado
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Sync data from PostgreSQL to MongoDB'

    def handle(self, *args, **kwargs):
        # Conectar a MongoDB
        client = MongoClient('mongodb+srv://1007220881:proyectoIcesi@sisd.vevqpo8.mongodb.net/')
        db = client['SISD']

        # Sincronizar datos de Pais
        for pais in Pais.objects.using('postgresql').all():
            db.paises.update_one(
                {'codigo': pais.codigo},
                {'$set': {'nombre': pais.nombre}},
                upsert=True
            )

        # Sincronizar datos de Departamento
        for departamento in Departamento.objects.using('postgresql').all():
            db.departamentos.update_one(
                {'codigo': departamento.codigo},
                {'$set': {'nombre': departamento.nombre, 'cod_pais': departamento.cod_pais.codigo}},
                upsert=True
            )

        # Sincronizar datos de Ciudad
        for ciudad in Ciudad.objects.using('postgresql').all():
            db.ciudades.update_one(
                {'codigo': ciudad.codigo},
                {'$set': {'nombre': ciudad.nombre, 'cod_dpto': ciudad.cod_dpto.codigo}},
                upsert=True
            )

        # Sincronizar datos de Sede
        for sede in Sede.objects.using('postgresql').all():
            db.sedes.update_one(
                {'codigo': sede.codigo},
                {'$set': {'nombre': sede.nombre, 'cod_ciudad': sede.cod_ciudad.codigo}},
                upsert=True
            )

        # Sincronizar datos de Lugar
        for lugar in Lugar.objects.using('postgresql').all():
            db.lugares.update_one(
                {'nombre': lugar.nombre},
                {'$set': {'direccion': lugar.direccion, 'ciudad': lugar.ciudad.codigo}},
                upsert=True
            )

        # Sincronizar datos de Empleado
        for empleado in Empleado.objects.using('postgresql').all():
            db.empleados.update_one(
                {'identificacion': empleado.identificacion},
                {'$set': {
                    'nombres': empleado.nombres,
                    'apellidos': empleado.apellidos,
                    'email': empleado.email,
                    'tipo_contratacion': empleado.tipo_contratacion.nombre,
                    'tipo_empleado': empleado.tipo_empleado.nombre,
                    'cod_facultad': empleado.cod_facultad.codigo,
                    'codigo_sede': empleado.codigo_sede.codigo,
                    'lugar_nacimiento': empleado.lugar_nacimiento.codigo,
                }},
                upsert=True
            )

        # Sincronizar datos de TipoContratacion
        for tipo_contratacion in TipoContratacion.objects.using('postgresql').all():
            db.tipo_contratacion.update_one(
                {'nombre': tipo_contratacion.nombre},
                {'$set': {}},
                upsert=True
            )

        # Sincronizar datos de TipoEmpleado
        for tipo_empleado in TipoEmpleado.objects.using('postgresql').all():
            db.tipo_empleado.update_one(
                {'nombre': tipo_empleado.nombre},
                {'$set': {}},
                upsert=True
            )

        # Sincronizar datos de Facultad
        for facultad in Facultad.objects.using('postgresql').all():
            db.facultades.update_one(
                {'codigo': facultad.codigo},
                {'$set': {
                    'nombre': facultad.nombre,
                    'ubicacion': facultad.ubicacion,
                    'nro_telefono': facultad.nro_telefono,
                    'id_decano': facultad.id_decano.identificacion if facultad.id_decano else None,
                }},
                upsert=True
            )

        # Sincronizar datos de Area
        for area in Area.objects.using('postgresql').all():
            db.areas.update_one(
                {'codigo': area.codigo},
                {'$set': {
                    'nombre': area.nombre,
                    'codigo_facultad': area.codigo_facultad.codigo,
                    'id_coordinador': area.id_coordinador.identificacion if area.id_coordinador else None,
                }},
                upsert=True
            )

        # Sincronizar datos de Programa
        for programa in Programa.objects.using('postgresql').all():
            db.programas.update_one(
                {'codigo': programa.codigo},
                {'$set': {
                    'nombre': programa.nombre,
                    'codigo_area': programa.codigo_area.codigo,
                }},
                upsert=True
            )

        # Sincronizar datos de Usuario
        for usuario in Usuario.objects.using('postgresql').all():
            db.usuarios.update_one(
                {'identificacion': usuario.identificacion},
                {'$set': {
                    'nombre_usuario': usuario.nombre_usuario,
                    'nombre_completo': usuario.nombre_completo,
                    'tipo_relacion': usuario.tipo_relacion,
                    'email': usuario.email,
                    'ciudad': usuario.ciudad.codigo,
                }},
                upsert=True
            )

        # Sincronizar datos de Evento
        for evento in Evento.objects.using('postgresql').all():
            db.eventos.update_one(
                {'titulo': evento.titulo},
                {'$set': {
                    'descripcion': evento.descripcion,
                    'categorias': evento.categorias,
                    'fecha': evento.fecha,
                    'lugar': evento.lugar.nombre,
                    'asistentes': [usuario.identificacion for usuario in evento.asistentes.all()],
                    'conferencistas': [usuario.identificacion for usuario in evento.conferencistas.all()],
                    'facultades_organizadoras': [facultad.codigo for facultad in evento.facultades_organizadoras.all()],
                    'programa_organizador': evento.programa_organizador.codigo if evento.programa_organizador else None,
                }},
                upsert=True
            )

        # Sincronizar datos de Comentario
        for comentario in Comentario.objects.using('postgresql').all():
            db.comentarios.update_one(
                {'evento': comentario.evento.titulo, 'usuario': comentario.usuario.identificacion},
                {'$set': {'texto': comentario.texto}},
                upsert=True
            )

        client.close()
