import requests
import sqlite3
from bs4 import BeautifulSoup
import pandas as pd



# region diccionarios

########FOTOS

#DICCIONARIO CON LAS URL DE CADA EQUIPO
urlTeamsLaligaFotos = {
    0: "atletico-madrid/startseite/verein/13/saison_id/2020",
    1: "fc-barcelona/startseite/verein/131/saison_id/2020",
    2: "real-madrid/startseite/verein/418/saison_id/2020",
    3: "fc-sevilla/startseite/verein/368/saison_id/2020",
    4: "real-sociedad-san-sebastian/startseite/verein/681/saison_id/2020",
    5: "fc-villarreal/startseite/verein/1050/saison_id/2020",
    6: "fc-valencia/startseite/verein/1049/saison_id/2020",
    7: "athletic-bilbao/startseite/verein/621/saison_id/2020",
    8: "real-betis-sevilla/startseite/verein/150/saison_id/2020",
    9: "fc-getafe/startseite/verein/3709/saison_id/2020",
    10: "fc-granada/startseite/verein/16795/saison_id/2020",
    11: "celta-vigo/startseite/verein/940/saison_id/2020",
    12: "ud-levante/startseite/verein/3368/saison_id/2020",
    13: "deportivo-alaves/startseite/verein/1108/saison_id/2020",
    14: "ca-osasuna/startseite/verein/331/saison_id/2020",
    15: "sd-eibar/startseite/verein/1533/saison_id/2020",
    16: "real-valladolid/startseite/verein/366/saison_id/2020",
    17: "sd-huesca/startseite/verein/5358/saison_id/2020",
    18: "cadiz-cf/startseite/verein/2687/saison_id/2020",
    19: "fc-elche/startseite/verein/1531/saison_id/2020"

}
#DICCIONARIO CON LOS NOMBRES DE LOS EQUIPOS
nombreEquiposFotos={

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


####NOTICIAS
nombreEquiposNoticias={

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
    19: "ELCHE",
    20: "GENERAL"

}
linkEquiposNoticias={

    0: "https://www.marca.com/futbol/atletico.html?intcmp=MENUESCU&s_kw=atletico",
    1: "https://www.marca.com/futbol/barcelona.html?intcmp=MENUESCU&s_kw=barcelona",
    2: "https://www.marca.com/futbol/real-madrid.html?intcmp=MENUESCU&s_kw=realmadrid",
    3: "https://www.marca.com/futbol/sevilla.html?intcmp=MENUESCU&s_kw=sevilla",
    4: "https://www.marca.com/futbol/real-sociedad.html?intcmp=MENUESCU&s_kw=realsociedad",
    5: "https://www.marca.com/futbol/villarreal.html?intcmp=MENUESCU&s_kw=villarreal",
    6: "https://www.marca.com/futbol/valencia.html?intcmp=MENUESCU&s_kw=valencia",
    7: "https://www.marca.com/futbol/athletic.html?intcmp=MENUESCU&s_kw=athletic",
    8: "https://www.marca.com/futbol/betis.html?intcmp=MENUESCU&s_kw=betis",
    9: "https://www.marca.com/futbol/getafe.html?intcmp=MENUESCU&s_kw=getafe",
    10: "https://www.marca.com/futbol/granada.html?intcmp=MENUESCU&s_kw=granada",
    11: "https://www.marca.com/futbol/celta.html?intcmp=MENUESCU&s_kw=celta",
    12: "https://www.marca.com/futbol/levante.html?intcmp=MENUESCU&s_kw=levante",
    13: "https://www.marca.com/futbol/alaves.html?intcmp=MENUESCU&s_kw=alaves",
    14: "https://www.marca.com/futbol/osasuna.html?intcmp=MENUESCU&s_kw=osasuna",
    15: "https://www.marca.com/futbol/eibar.html?intcmp=MENUESCU&s_kw=eibar",
    16: "https://www.marca.com/futbol/valladolid.html?intcmp=MENUESCU&s_kw=valladolid",
    17: "https://www.marca.com/futbol/huesca.html?intcmp=MENUESCU&s_kw=huesca",
    18: "https://www.marca.com/futbol/cadiz.html?intcmp=MENUESCU&s_kw=cadiz",
    19: "https://www.marca.com/futbol/elche.html?intcmp=MENUESCU&s_kw=elche",
    20: "https://www.marca.com/futbol/primera-division.html?intcmp=MENUMIGA&s_kw=laliga-santander"

}

####TABLAS
#DICCIONARIO CON LOS NOMBRES DE LOS EQUIPOS
nombreEquiposTablas={

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
equipos_estadisticasTablas = {
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





# endregion

# region bases de datos

con = sqlite3.connect('equipos.db')
cursorObj=con.cursor()


#borra las tablas si tenian algo

cursorObj.execute('DROP table if exists ASISTENCIAS')
cursorObj.execute('DROP table if exists CLASIFICACION')
cursorObj.execute('DROP table if exists FOTOS')
cursorObj.execute('DROP table if exists GOLEADORES_EQUIPOS')
cursorObj.execute('DROP table if exists GOLES_ENCAJADOS')
cursorObj.execute('DROP table if exists NOTICIAS')
cursorObj.execute('DROP table if exists PICHICHI')


try:
    ############FOTOS
    cursorObj.execute('''CREATE TABLE FOTOS(Equipo TEXT, Nombre TEXT, LinkFoto TEXT)''')  # comentar una vez ejecutadi
    ############NOTICIAS
    cursorObj.execute(
        '''CREATE TABLE NOTICIAS(Titulo TEXT, Foto TEXT, Contenido TEXT, Equipo TEXT)''')  # comentar una vez creadas las tablas
    ############TABLAS
    cursorObj.execute('''CREATE TABLE CLASIFICACION (Equipo TEXT, Puntos INT)''')  # comentar una vez ejecutado
    cursorObj.execute('''CREATE TABLE PICHICHI (Nombre TEXT, Goles INT)''')  # comentar una vez ejecutado
    cursorObj.execute('''CREATE TABLE ASISTENCIAS (Nombre TEXT, Asistencias INT)''')  # comentar una vez ejecutado
    cursorObj.execute(
        '''CREATE TABLE GOLES_ENCAJADOS (Nombre TEXT, Goles_encajados INT)''')  # comentar una vez ejecutado
    cursorObj.execute(
        '''CREATE TABLE GOLEADORES_EQUIPOS (Equipo TEXT, Nombre TEXT, Goles INT)''')  # comentar una vez ejecutado
    con.commit()  # comentar una vez ejecutado

except:
    con.commit()



#PASAR A DB FOTOS
def pasarAdbFotos(equipo,jugador,linkfoto):


    i=0
    while i < len(equipo):
        con.execute('''INSERT INTO FOTOS(Equipo,Nombre,LinkFoto) VALUES(?, ?, ?)''',
                    (str(equipo[i]), str(jugador[i]), str(linkfoto[i])))

        con.commit()
        i=i+1;

    print("Informacion migrada a la DB")
#PASAR A DB NOTICIAS
def pasarAdbNoticias(titulo,foto,contenido,equipo):

    i=0
    while i < len(titulo):
        con.execute('''INSERT INTO NOTICIAS(titulo,Foto,Contenido,Equipo) VALUES(?, ?, ?,?)''',
                    (str(titulo[i]), str(foto[i]), str(contenido[i]), str(equipo[i])))

        con.commit()
        i=i+1;

    print("Informacion migrada a la DB")
#PASAR A DB TABLAS
def pasar_DB1(columna1, columna2, tabla, nombre_columna1, nombre_columna2):

    i = 0


    while i < len(columna1):
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

# region fotos

#variables
urlTransfermark = "https://www.transfermarkt.es/"
PlayersList = list()
linklist = list()
listaFotos = list()
listaEquipos = list()


#funciones

def scrapeofoto(indice,links,nombres,listafotos):

    url=links[indice]

    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    fotoscarnet=pageSoup.find_all("div",{"class": "dataBild"})[0].find_all("img")

    try:
        fotos=pageSoup.find_all("div",{"class": "galerie-content"})[0].find_all("img")
        listafotos.append(fotos[0]['data-src'])

    except:
        listafotos.append(fotoscarnet[0]['src'])
def scrapeoFotos(url, players,links,equipo,listaequipos):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    player = pageSoup.find_all("td", {"itemprop": "athlete"})

    link = pageSoup.select("td[class='hauptlink']",href=True)

    for i in link:

        links.append("https://www.transfermarkt.es"+i.find_all("a")[0]['href'])


    for i in player:
        players.append(i.text)
        listaEquipos.append(nombreEquiposFotos[equipo])

#Main

for clave in urlTeamsLaligaFotos:

    valor= nombreEquiposFotos[clave]
    print('.')
    scrapeoFotos(urlTransfermark + urlTeamsLaligaFotos[clave], PlayersList,linklist,clave,listaEquipos)

cont=0
for i in PlayersList:
    scrapeofoto(cont, linklist, PlayersList,listaFotos)
    print(i+"--"+listaEquipos[cont]+"---"+listaFotos[cont])
    cont= cont+1

pasarAdbFotos(listaEquipos,PlayersList,listaFotos)


# endregion

# region noticias
#VARIABLES

titulos=list()
fotos=list()
contenidos=list()
equipos=list()



#FUNCIONES
def scrapeonoticia(url, titulo,foto,contenido,cantidad,equipolista,equipo):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    links = list()

    link = pageSoup.select("li[class='content-item']",href=True)


#saco los links de las noticias, si generan algun error entonces no los coge
    cont=0
    i=0

    while cont<cantidad:
        try:
            print("noticias de " + equipo)

            links.append(link[i].find_all("a")[0]['href']) #append del link
            pageTree2 = requests.get(links[i], headers=header)
            pageSoup2 = BeautifulSoup(pageTree2.content, 'html.parser')

            #---prueba titulos
            #print(pageSoup2.find_all("h1", {"class": "ue-c-article__headline"})[0].text)
            titulos.append(pageSoup2.find_all("h1", {"class": "ue-c-article__headline"})[0].text)

            #---prueba fotos
            try:
                fotos.append(pageSoup2.find_all("img", {"class": "ue-c-article__media--image"})[0]['src'])
                # print(pageSoup.find_all("img", {"class": "ue-c-article__media--image"})[0]['src'])
            except:
                fotos.append("https://e00-marca.uecdn.es/assets/v21/img/destacadas/marca__logo-generica.jpg")

            #---prueba contenido
            contenido.append(pageSoup2.find_all("div", {"class": "ue-c-article__body"})[0].text)

            #print(pageSoup2.find_all("div", {"class": "ue-c-article__body"})[0].text)

            equipolista.append(equipo)#append del equipo

            cont+=1
            i+=1

        except:
            print("pasando")
            i+=1


#MAIN
#LLAMADA A LA FUNCION DE SCRAPEO PARA CADA EQUIPO
for i in range(21):

    scrapeonoticia(linkEquiposNoticias[i], titulos, fotos, contenidos,5, equipos, nombreEquiposNoticias[i])

pasarAdbNoticias(titulos,fotos,contenidos,equipos)


# endregion

# region tablas

#FUNCIONES

def scrapeoTablas(url,listajugadores,listadatos,cantidad):




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
    page = requests.get(equipos_estadisticasTablas[numequipo], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
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
        listaequipos.append(nombreEquiposTablas[numequipo])


#MAIN

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
scrapeoTablas('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles/',goleadores,goles,20)

print("TABLA DE GOLEADORES")
for i in range(20):
    print(f' {i+1}- {goleadores[i]}  {goles[i]} ')

pasar_DB1(goleadores,goles,"PICHICHI","Nombre","Goles")


#ASISTENCIAS

asistentes=list()
asistencias=list()
scrapeoTablas('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/asistencias-de-gol/',asistentes,asistencias,20)

print("TABLA DE ASISTENCIAS")
for i in range(20):
    print(f' {i+1}- {asistentes[i]}  {asistencias[i]} ')

pasar_DB1(asistentes,asistencias,"ASISTENCIAS","Nombre","Asistencias")

#GOLES ENCAJADOS


porteros=list()
encajados=list()
scrapeoTablas('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles-encajados/',porteros,encajados,20)

print("TABLA DE GOLES ENCAJADOS")
for i in range(20):
    print(f' {i+1}- {porteros[i]}  {encajados[i]} ')


pasar_DB1(porteros,encajados,"GOLES_ENCAJADOS","Nombre","Goles_encajados")



# endregion

# endregion

