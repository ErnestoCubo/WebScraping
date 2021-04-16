import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from operator import itemgetter








# region BDS





'''
- TABLA PARA CLASIFICACION  {EQUIPO,PTOS, TABLA}
- TABLA PICHICHI GENERALES  {EQUIPO,NOMBRE,GOLES, TABLA}
- TABLA ASISTENTES GENERALES {EQUIPO,NOMBRE,ASISTENCIAS, TABLA}
-TABLA ENCAJADOS GENERALES  {EQUIPO,NOMBRE,ENCAJADOS, TABLA}


-TABLA GOLEADORES EQUIPOS {EQUIPO,NOMBRE,GOLES, TABLA}



'''



con = sqlite3.connect('pruebas.db')
cursorObj=con.cursor()
cursorObj.execute('''CREATE TABLE CLASIFICACION (Equipo TEXT, Puntos INT)''')#comentar una vez ejecutado
cursorObj.execute('''CREATE TABLE PICHICHI (Nombre TEXT, Goles INT)''')#comentar una vez ejecutado
cursorObj.execute('''CREATE TABLE ASISTENCIAS (Nombre TEXT, Asistencias INT)''')#comentar una vez ejecutado
cursorObj.execute('''CREATE TABLE GOLES_ENCAJADOS (Nombre TEXT, Goles_encajados INT)''')#comentar una vez ejecutado
cursorObj.execute('''CREATE TABLE GOLEADORES_EQUIPOS (Equipo TEXT, Nombre TEXT, Goles INT)''')#comentar una vez ejecutado
con.commit()



def pasar_DB1(columna1, columna2, tabla, nombre_columna1, nombre_columna2):

    i = 0


    while i < len(equipo):
        con.execute(f'INSERT INTO {tabla}({nombre_columna1},{nombre_columna2}) VALUES(?, ?)',
                    (str(columna1[i]), int(columna2[i])))

        con.commit()
        i = i + 1;

    print("Informacion migrada a la DB")



#goleadores equipo
def pasar_DB2(equipo, nombre, tabla, columna,nombre_columna):

    i = 0

    while i < len(equipo):
        con.execute(f'INSERT INTO {tabla} (Equipo,Nombre,{nombre_columna}) VALUES(?, ?, ?)',
                    (str(equipo[i]), str(nombre[i]), int(columna[i])))

        con.commit()
        i = i + 1;

    print("Informacion migrada a la DB")



# endregion

#DICCIONARIO CON LOS NOMBRES DE LOS EQUIPOS
nombreEquipos={

    0: "ATLETICO",
    1: "BARCELONA",
    2: "REAL MADRID",
    3: "SEVILLA",
    4: "REAL SOCIEDAD",
    5: "VILLARREAL",
    6: "VALENCIA",
    7: "ATHLETIC",
    8: "BETIS",
    9: "GETAFE",
    10: "GRANADA",
    11: "CELTA",
    12: "LEVANTE",
    13: "ALAVES",
    14: "OSASUNA",
    15: "EIBAR",
    16: "VALLADOLID",
    17: "HUESCA",
    18: "CADIZ",
    19: "ELCHE"



}
#Diccionario con los links
equipos_estadisticas = {
    0: "https://resultados.as.com/resultados/ficha/equipo/atletico/42/2020/estadisticas/primera/",
    1: "https://resultados.as.com/resultados/ficha/equipo/barcelona/3/2020/estadisticas/primera/",
    2: "https://resultados.as.com/resultados/ficha/equipo/real_madrid/1/2020/estadisticas/primera/",
    3: "https://resultados.as.com/resultados/ficha/equipo/sevilla/53/2020/estadisticas/primera/",
    4: "https://resultados.as.com/resultados/ficha/equipo/r_sociedad/16/2020/estadisticas/primera/",
    5: "https://resultados.as.com/resultados/ficha/equipo/villarreal/19/2020/estadisticas/primera/",
    6: "https://resultados.as.com/resultados/ficha/equipo/valencia/17/2020/estadisticas/primera/",
    7: "https://resultados.as.com/resultados/ficha/equipo/athletic/5/2020/estadisticas/primera/",
    8: "https://resultados.as.com/resultados/ficha/equipo/betis/171/2020/estadisticas/primera/",
    9: "https://resultados.as.com/resultados/ficha/equipo/getafe/172/2020/estadisticas/primera/",
    10: "https://resultados.as.com/resultados/ficha/equipo/granada/347/2020/estadisticas/primera/",
    11: "https://resultados.as.com/resultados/ficha/equipo/celta/6/2020/estadisticas/primera/",
    12: "https://resultados.as.com/resultados/ficha/equipo/levante/136/2020/estadisticas/primera/",
    13: "https://resultados.as.com/resultados/ficha/equipo/alaves/4/2020/estadisticas/primera/",
    14: "https://resultados.as.com/resultados/ficha/equipo/osasuna/13/2020/estadisticas/primera/",
    15: "https://resultados.as.com/resultados/ficha/equipo/eibar/108/2020/estadisticas/primera/",
    16: "https://resultados.as.com/resultados/ficha/equipo/valladolid/18/2020/estadisticas/primera/",
    17: "https://resultados.as.com/resultados/ficha/equipo/huesca/864/2020/estadisticas/primera/",
    18: "https://resultados.as.com/resultados/ficha/equipo/cadiz/91/2020/estadisticas/primera/",
    19: "https://resultados.as.com/resultados/ficha/equipo/elche/121/2020/estadisticas/primera/"

}




def scrapeo(url,listajugadores,listadatos,cantidad):




    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    jugador=soup.find_all('span',class_='name')
    dato=soup.find_all('td',class_='cantidad')

    cont=0;



    for i in jugador:
        if cont==cantidad:
            break;
        listajugadores.append(i.text)
        cont=cont+1;
    cont=0;
    for i in dato:
        if cont==cantidad:
            break;
        if cont==0:
            listadatos.append(i.text[0:2])
        else:
            listadatos.append(i.text)

        cont=cont+1;

def est_equipo(numequipo,listajugs,listagoles,listaequipos):
    page = requests.get(equipos_estadisticas[numequipo], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    jugador=soup.find_all('span',class_='player-inline')
    goles=soup.find_all('tbody')[1].find_all('td')
    goleadoresequipo1=list()
    golescont=0;
    aux=list()

    for i in range(int(len(goles)/3)):
        aux.append(list());
        aux[i].append(jugador[i].text)
        aux[i].append(int(goles[golescont].text))
        golescont=golescont+3;
    goleadoresequipo1.append(sorted(aux, key=lambda x: x[1],reverse=True))


    cont=0
    for i in range(5):
        #print(goleadoresequipo1[0][i][0])
        listajugs.append(goleadoresequipo1[0][i][0])
        listagoles.append(goleadoresequipo1[0][i][1])
        listaequipos.append(nombreEquipos[numequipo])




# region estadisticas individuales de equipo

jugadores=list()
goles=list()
equipos=list()


for i in range(20):
    est_equipo(i, jugadores, goles, equipos)

for i in range(len(jugadores)):
    print(f'{jugadores[i]}--{goles[i]}--{equipos[i]}')





pasar_DB2(equipos,jugadores,"GOLEADORES_EQUIPOS",goles,"Goles")



# endregion



# region generales


#scrapeo clasificacion

equipos=list()
ptos=list()
golesf=list()
golesc=list()

page = requests.get('https://resultados.as.com/resultados/futbol/primera/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
soup = BeautifulSoup(page.content, 'html.parser')


equipo = soup.find_all('a', class_='nombre-equipo')
puntos = soup.find_all('td', class_='destacado')




for i in puntos:
    ptos.append(i.text)


for i in equipo:
    equipos.append(i.text.rstrip('\n')[1:])


for i in range(20):
    print(f'{i+1}-     {equipos[i]}      {ptos[i]}')


pasar_DB1(equipos,ptos,"CLASIFICACION","Equipo","Puntos")





#goleadores

goleadores=list()
goles=list()
scrapeo('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles/',goleadores,goles,20)

print("TABLA DE GOLEADORES")
for i in range(20):
    print(f' {i+1}- {goleadores[i]}  {goles[i]} ')

pasar_DB1(goleadores,goles,"PICHICHI","Nombre","Goles")


#ASISTENCIAS

asistentes=list()
asistencias=list()
scrapeo('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/asistencias-de-gol/',asistentes,asistencias,20)

print("TABLA DE ASISTENCIAS")
for i in range(20):
    print(f' {i+1}- {asistentes[i]}  {asistencias[i]} ')

pasar_DB1(asistentes,asistencias,"ASISTENCIAS","Nombre","Asistencias")

#GOLES ENCAJADOS


porteros=list()
encajados=list()
scrapeo('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles-encajados/',porteros,encajados,20)

print("TABLA DE GOLES ENCAJADOS")
for i in range(20):
    print(f' {i+1}- {porteros[i]}  {encajados[i]} ')


pasar_DB1(porteros,encajados,"GOLES_ENCAJADOS","Nombre","Goles_encajados")



# endregion









