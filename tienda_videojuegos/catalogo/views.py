from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalogo.models import Juego


# Create your views here.
def lista_juegos(request):
    juegos = Juego.objects.all()

    paginator = Paginator(juegos,6)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    contexto_catalogo_juegos = {'lista_juegos': page_obj}

    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)



def detalle_juego(request, pk):
    # Obtiene el juego concreto o muestra 404 si no existe
    juego = get_object_or_404(Juego, pk=pk)

    # Creamos el contexro que se pasa a la plantilla
    contexto = {'juego' : juego}

    # Renderiza la plantilla de detalle
    return render(request, 'catalogo/detalle_juego.html' , contexto)