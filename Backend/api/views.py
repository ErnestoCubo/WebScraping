from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JugadorSerializer
from .models import Jugadores
from .models import EQUIPOS
from .serializers import EquiposSerializer
from bs4 import BeautifulSoup
import pandas as pd
import requests


# Create your views here.

class JugadorView(viewsets.ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugadores.objects.all()

class EquipoView(viewsets.ModelViewSet):
    serializer_class = EquiposSerializer
    queryset = EQUIPOS.objects.all()

def execu(request):
  
    exec(open('/Users/piopio/Desktop/Uni/django-react/BackEnd_django/api/mediascr.py').read())
    print('holiwi')
    return HttpResponse("Ojala se ejecute algo")