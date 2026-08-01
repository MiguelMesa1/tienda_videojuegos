from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages


def registro_view(request): # Definimos la vista.
    if request.method == 'POST': # Revisa si envio el formulario
         # Crear un objeto del formulario RegistroForm con la info que usuario escribio en los campos ese objeto se encuentra en forms.py
        form = RegistroForm(request.POST)
        if form.is_valid(): # Validar el formulario/ Django revisa que se cumplan las reglas del modelo
            usuario = form.save() # Guardar nuevo usuario si los datos son validos.
            login(request, usuario) # despues de registrar al usuario hace automaticamente login.
            messages.success(request, "Registro completado correctamente.")
            return redirect('home') # redirecciona a la url home
        messages.success(request, "Registro completado correctamente.")
    else: # hace un get
        form = RegistroForm() # carga el formulario vacio 
    return render( request,'usuarios/registro.html',{'form': form}) # devuelve la plantilla de registro

def login_view(request):
    if request.method == 'POST': # Revisa si envio el formulario
        # Instancia de tipo login form pasandole el objeto request de la solicitud como lo que envio el usuario en el request.POST
        form = LoginForm(request, data=request.POST) 

        if form.is_valid(): #Comprueba credenciales en la base de datos para ver si los datos coinciden
            usuario = form.get_user() # Obtiene el objeto usuario correspondiente
            login(request, usuario) # Registra el usuario en la sesión permitiendo que acceda a las vistas protegidas
            messages.success(request, "Inicio de sesión correcto.")
            return redirect('home') # Redirige ala Url Home
        else:
            # Mostrar errores generales en consola para debug
            print(form.errors)
            messages.error(request,"Usuario o contraseña incorrectos.")
    else:
        form = LoginForm() # Cargar el formulario vacio
    return render(request,'usuarios/login.html',{'form': form}) # Solicitar que se cargue la plantilla


# Cerrar sesión
def logout_view(request):
    logout(request) # Solicitud para cerrar sesión
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login') #Redirigir a la página login

@login_required
def perfil_view(request):
    return render(request, 'usuarios/perfil.html')