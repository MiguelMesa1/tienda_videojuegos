from django.urls import path
from . import views

urlpatterns = [
 #ruta contacto: Llama a la vista de contacto
    path('', views.lista_juegos, name='lista_juegos')
]