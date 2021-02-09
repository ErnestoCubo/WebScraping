import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3



def scrapeo(url,listajugadores,listadatos):




    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    jugador=soup.find_all('span',class_='name')
    dato=soup.find_all('td',class_='cantidad')

    cont=0;



    for i in jugador:
        if cont==20:
            break;
        listajugadores.append(i.text)
        cont=cont+1;
    cont=0;
    for i in dato:
        if cont==20:
            break;
        listadatos.append(i.text)
        cont=cont+1;



#goleadores

goleadores=list()
goles=list()
scrapeo('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles/',goleadores,goles)

print("TABLA DE GOLEADORES")
for i in range(20):
    print(f' {i+1}- {goleadores[i]}  {goles[i]} ')


#ASISTENCIAS

asistentes=list()
asistencias=list()
scrapeo('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/asistencias-de-gol/',asistentes,asistencias)

print("TABLA DE ASISTENCIAS")
for i in range(20):
    print(f' {i+1}- {asistentes[i]}  {asistencias[i]} ')

#GOLES ENCAJADOS

porteros=list()
encajados=list()
scrapeo('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles-encajados/',porteros,encajados)

print("TABLA DE GOLES ENCAJADOS")
for i in range(20):
    print(f' {i+1}- {porteros[i]}  {encajados[i]} ')








