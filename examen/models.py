from django.db import models

# Create your models here.

class MiniJuego (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    PLATAFORMAS = [
        ("PS4", "Play Staytions"),
        ("XBOX", "Xbox Series"),
        ("SWITCH", "Nintendo Switch"),
    ]
    platafroma = models.CharField(choices=PLATAFORMAS, max_length=50),
    fecha_lanzamiento = models.DateField()
    
class Cuenta_Bancaria (models.Model):
    numero_cuenta = models.IntegerField()
    BANCOS = [
        ("ING", "Banco ING"),
        ("UNICAJA", "Banco UNICAJA"),
        ("CAIXA", "Banco CAIXA"),
        ("BBVA", "Banco BBVA"),
    ]
    banco = models.CharField(choices=BANCOS, max_length=100)
    
class Usuario (models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    edad = models.CharField(max_length=10)
    correo = models.EmailField()
    #1 usuarios pueden tener 1 unica cuenta bancaria.
    cuenta_bancaria = models.OneToOneField(Cuenta_Bancaria, on_delete=models.CASCADE, related_name="cuenta_bancaria_usuario")
    
class Voto (models.Model):
    puntuacion = models.IntegerField()
    comentario = models.CharField(max_length=50)
    fecha_hora = models.DateField()
    #1 o varios ususario puede votar 1 vez a un juego (1:N)
    usuario_voto = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ususario_que_voto")
    #1 minijuego puede ser votado 1 o muchas veces y un voto puede estar en 1 o varios minijuegos(N:N)
    minijuego_voto = models.ManyToManyField(MiniJuego, related_name="minijuego_que_se_voto", through='votos_de_los_minijuegos')
    
class Votos_de_los_minijuegos (models.Model):
    id_voto = models.ForeignKey(Voto, on_delete=models.CASCADE)
    id_minijuego = models.ForeignKey(MiniJuego, on_delete=models.CASCADE)