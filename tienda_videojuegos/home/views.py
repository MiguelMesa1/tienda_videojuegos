from django.shortcuts import render

# Vista página principal
def index(request):
    # Render toma el request y el html que se va a mostrar
    return render(request, "home/index.html")

# Vista página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')