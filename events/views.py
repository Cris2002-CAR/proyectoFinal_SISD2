
from django.shortcuts import render, get_object_or_404
from .models import Evento, Usuario, Empleado, Comentario
from django.shortcuts import redirect
from django.db import connection
from .forms import UploadSQLFileForm

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    asistentes = evento.asistentes.all()
    conferencistas = evento.conferencistas.all()
    facultades_organizadoras = evento.facultades_organizadoras.all()
    comentarios = Comentario.objects.filter(evento=evento)
    
    contexto = {
        'evento': evento,
        'asistentes': asistentes,
        'conferencistas': conferencistas,
        'facultades_organizadoras': facultades_organizadoras,
        'comentarios': comentarios
    }
    
    return render(request, 'detalle_evento.html', contexto)


def upload_sql_file(request):
    if request.method == 'POST':
        form = UploadSQLFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            sql_statements = file.read().decode('utf-8')
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql_statements)
                return render(request, 'upload_success.html')
            except Exception as e:
                return render(request, 'upload_fail.html', {'error': str(e)})
    else:
        form = UploadSQLFileForm()
    return render(request, 'upload_sql_file.html', {'form': form})
