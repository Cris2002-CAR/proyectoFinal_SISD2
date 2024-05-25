
from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.listar_eventos, name='listar_eventos'),
]
