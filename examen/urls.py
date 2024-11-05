from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('Voto/ultimo_voto_minijuego_en_concreto/<int:id_minijuego>', views.ultimo_voto_minijuego_en_concreto, name = 'ultimo_voto_minijuego_en_concreto'),
    path('Minijuego/minijuegos_votos_menor_3/<int:id_usuario>', views.minijuegos_votos_menor_3, name ='minijuegos_votos_menor_3'),
    path('Usuario/usuario_nunca_votaron', views.usuario_nunca_votaron, name = 'usuario_nunca_votaron')
]
