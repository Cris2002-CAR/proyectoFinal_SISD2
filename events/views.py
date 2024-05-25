# app/views.py

from django.shortcuts import render
from .models import Evento

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})
