from django.http import HttpResponse

def index(request):
    # Solo para depurar, prueba con una respuesta simple:
    return HttpResponse("¡Hola, mundo!")
