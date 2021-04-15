from rest_framework import serializers
from .models import Jugadores
from .models import EQUIPOS

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('jugador', 'edad', 'pais', 'equipos', 'dorsal', 'posicion', 'precio', 'actualizacion')
class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = EQUIPOS
        fields = ('Equipo', 'Jugadores', 'EdadMedia', 'ValorTotal', 'ValorMedio', 'Actualizacion')
