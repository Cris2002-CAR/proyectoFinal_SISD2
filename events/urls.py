
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('upload_sql/', views.upload_sql_file, name='upload_sql_file'),
]
