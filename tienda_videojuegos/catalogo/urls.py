from django.urls import path
from . import views

# Sirve para poder construir Urls de una manera mas legible 
app_name = 'catalogo'

urlpatterns = [
 #ruta contacto: Llama a la vista de contacto
    path('', views.lista_juegos, name='lista_juegos'),
    path('<int:pk>/', views.detalle_juego, name='detalle_juego')
]