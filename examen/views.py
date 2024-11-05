from django.shortcuts import render
from .models import *
from django.db.models import Q,Prefetch

# Create your views here.

def inicio (request):
    return render(request, 'index.html')

def ultimo_voto_minijuego_en_concreto (request, id_minijuego):
    voto = Voto.objects.prefetch_related(
        "minijuego_que_se_voto",
        "usuario_voto"
    ).filter(votos_de_los_minijuegos__id_minijuego = id_minijuego).order_by('-fecha_hora')[1]
    return render(request, 'Voto/ultimo_voto_minijuego_en_concreto.html', {"voto": voto})

def minijuegos_votos_menor_3 (request, id_usuario):
    minijuegos = MiniJuego.objects.prefetch_related("minijuego_que_se_voto").filter(
    Q(minijuego_que_se_voto__usuario_voto = id_usuario) & Q(minijuego_que_se_voto__puntuacion__lte = 3)
    ).all()
    return render(request, 'Minijuegos/minijuegos_votos_menor_3.html', {"minijuegos": minijuegos})

def usuario_nunca_votaron (request):
    usuario = Usuario.objects.select_related('  ususario_que_voto', 'cuenta_bancaria_usuario').filter(
        ususario_que_voto = None
    ).all()
    return render(request, 'Usuario/usuario_nunca_votaron.html', {"usuario": usuario})