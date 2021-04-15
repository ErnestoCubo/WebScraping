import requests
import sqlite3

from bs4 import BeautifulSoup

import pandas as pd



#CREACION DE LA TABLA Y LAS COLUMNAS

con = sqlite3.connect('equipos.db')
cursorObj=con.cursor()
cursorObj.execute('''CREATE TABLE NOTICIAS(Titulo TEXT, Foto TEXT, Contenido TEXT, Equipo TEXT)''')#comentar una vez creadas las tablas
con.commit()#comentar una vez creadas las tablas

#LISTAS QUE SE VAN A USAR

titulos=list()
fotos=list()
contenidos=list()
equipos=list()

#DICCIONARIOS QUE SE VAN A USAR
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
    19: "ELCHE",
    20: "GENERAL"

}
linkEquipos={

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


#FUNCION DE PASAR A LA BASE DE DATOS
def pasarAdb(titulo,foto,contenido,equipo):

    i=0
    while i < len(titulo):
        con.execute('''INSERT INTO NOTICIAS(titulo,Foto,Contenido,Equipo) VALUES(?, ?, ?,?)''',
                    (str(titulo[i]), str(foto[i]), str(contenido[i]), str(equipo[i])))

        con.commit()
        i=i+1;

    print("Informacion migrada a la DB")


#FUNCION DE SCRAPING DE LAS NOTICIAS
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



#LLAMADA A LA FUNCION DE SCRAPEO PARA CADA EQUIPO
for i in range(21):

    scrapeonoticia(linkEquipos[i], titulos, fotos, contenidos,5, equipos, nombreEquipos[i])





pasarAdb(titulos,fotos,contenidos,equipos)

