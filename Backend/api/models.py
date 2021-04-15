from django.db import models

# Create your models here.
# from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Jugadores(models.Model):
    jugador = models.TextField(max_length=120)
    edad = models.IntegerField()
    pais = models.TextField(max_length=120)
    equipos = models.TextField(max_length=120)
    dorsal = models.IntegerField()
    posicion = models.TextField(max_length=120)
    precio = models.FloatField()
    actualizacion = models.TextField(max_length=120)



    def _str_(self):
        return self.jugador

class EQUIPOS(models.Model):
    Equipo =models.TextField(max_length=120)
    Jugadores = models.IntegerField()
    EdadMedia = models.IntegerField()
    ValorTotal = models.FloatField()
    ValorMedio = models.FloatField()
    Actualizacion = models.TextField(max_length=120)

    def _str_(self):
        return self.Equipo