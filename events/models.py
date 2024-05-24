from django.db import models

class Pais(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        db_table = 'eventos_paises'


class Departamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    cod_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos_departamentos'


class Ciudad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    cod_dpto = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos_ciudades'


class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos_lugares'


class TipoContratacion(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

    class Meta:
        db_table = 'eventos_tipos_contratacion'


class TipoEmpleado(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

    class Meta:
        db_table = 'eventos_tipos_empleado'


class Facultad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=15)
    nro_telefono = models.CharField(max_length=15)
    id_decano = models.OneToOneField('Empleado', null=True, blank=True, on_delete=models.SET_NULL, related_name='decano_facultad')

    class Meta:
        db_table = 'eventos_facultades'


class Empleado(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    tipo_contratacion = models.ForeignKey(TipoContratacion, on_delete=models.CASCADE)
    tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    cod_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    codigo_sede = models.ForeignKey('Sede', on_delete=models.CASCADE)
    lugar_nacimiento = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos_empleados'


class Area(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    codigo_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    id_coordinador = models.OneToOneField(Empleado, on_delete=models.CASCADE, related_name='coordinador_area')

    class Meta:
        db_table = 'eventos_areas'
        unique_together = (('id_coordinador',),)


class Programa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    codigo_area = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos_programas'


class Sede(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    cod_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos_sedes'


class Usuario(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    nombre_completo = models.CharField(max_length=60)
    tipo_relacion = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos_usuarios'


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categorias = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    asistentes = models.ManyToManyField(Usuario, related_name='asistentes')
    conferencistas = models.ManyToManyField(Usuario, related_name='conferencistas')
    facultades_organizadoras = models.ManyToManyField(Facultad)
    programa_organizador = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'eventos_eventos'


class Comentario(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()

    class Meta:
        db_table = 'eventos_comentarios'
