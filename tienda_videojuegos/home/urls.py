from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # ruta principal: Llama a la vista index
    path('contacto/', views.contacto, name='contacto') #ruta contacto: Llama a la vista de contacto
]