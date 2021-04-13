
import requests
import sqlite3

from bs4 import BeautifulSoup

import pandas as pd


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


def scrapeo(url, players,links,equipo,listaequipos):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    player = pageSoup.find_all("td", {"itemprop": "athlete"})

    link = pageSoup.select("td[class='hauptlink']",href=True)



    for i in link:

        links.append("https://www.transfermarkt.es"+i.find_all("a")[0]['href'])


    for i in player:
        players.append(i.text)
        listaEquipos.append(nombreEquipos[equipo])




con = sqlite3.connect('equipos.db')
cursorObj=con.cursor()
#cursorObj.execute('''CREATE TABLE FOTOS(Equipo TEXT, Nombre TEXT, LinkFoto TEXT)''')#comentar una vez ejecutadi
#con.commit()#


def pasarAdb(equipo,jugador,linkfoto):





    i=0
    while i < len(equipo):
        con.execute('''INSERT INTO FOTOS(Equipo,Nombre,LinkFoto) VALUES(?, ?, ?)''',
                    (str(equipo[i]), str(jugador[i]), str(linkfoto[i])))

        con.commit()
        i=i+1;

    print("Informacion migrada a la DB")







#DICCIONARIO CON LAS URL DE CADA EQUIPO
urlTeamsLaliga = {
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
#ESTO DE MOMENTO NO SE USA PERO PODRIA USARSE EN UN FUTURO
urlfotos = {
    0: "https://www.transfermarkt.es/atletico-madrid/kader/verein/13/saison_id/2020/galerie/1/page/",
    1: "https://www.transfermarkt.es/fc-barcelona/kader/verein/131/saison_id/2020/galerie/1/page/",
    2: "https://www.transfermarkt.es/real-madrid/kader/verein/418/saison_id/2020/galerie/1/page/",
    3: "https://www.transfermarkt.es/fc-sevilla/kader/verein/368/saison_id/2020/galerie/1/page/",
    4: "https://www.transfermarkt.es/real-sociedad-san-sebastian/kader/verein/681/saison_id/2020/galerie/1/page/",
    5: "https://www.transfermarkt.es/fc-villarreal/kader/verein/1050/saison_id/2020/galerie/1/page/",
    6: "https://www.transfermarkt.es/fc-valencia/kader/verein/1049/saison_id/2020/galerie/1/page/",
    7: "https://www.transfermarkt.es/athletic-bilbao/kader/verein/621/saison_id/2020/galerie/1/page/",
    8: "https://www.transfermarkt.es/real-betis-sevilla/kader/verein/150/saison_id/2020/galerie/1/page/",
    9: "https://www.transfermarkt.es/fc-getafe/kader/verein/3709/saison_id/2020/galerie/1/page/",
    10: "https://www.transfermarkt.es/fc-granada/kader/verein/16795/saison_id/2020/galerie/1/page/",
    11: "https://www.transfermarkt.es/celta-vigo/kader/verein/940/saison_id/2020/galerie/1/page/",
    12: "https://www.transfermarkt.es/ud-levante/kader/verein/3368/saison_id/2020/galerie/1/page/",
    13: "https://www.transfermarkt.es/deportivo-alaves/kader/verein/1108/saison_id/2020/galerie/1/page/",
    14: "https://www.transfermarkt.es/ca-osasuna/kader/verein/331/saison_id/2020/galerie/1/page/",
    15: "https://www.transfermarkt.es/sd-eibar/kader/verein/1533/saison_id/2020/galerie/1/page/",
    16: "https://www.transfermarkt.es/real-valladolid/kader/verein/366/saison_id/2020/galerie/1/page/",
    17: "https://www.transfermarkt.es/sd-huesca/kader/verein/5358/saison_id/2020/galerie/1/page/",
    18: "https://www.transfermarkt.es/cadiz-cf/kader/verein/2687/saison_id/2020/galerie/1/page/",
    19: "https://www.transfermarkt.es/fc-elche/kader/verein/1531/saison_id/2020/galerie/1/page/"

}



urlTransfermark = "https://www.transfermarkt.es/"

PlayersList = list()
linklist = list()
listaFotos = list()
listaEquipos = list()


for clave in urlTeamsLaliga:

    valor= nombreEquipos[clave]
    print('.')
    scrapeo(urlTransfermark + urlTeamsLaliga[clave], PlayersList,linklist,clave,listaEquipos)

cont=0
for i in PlayersList:
    scrapeofoto(cont, linklist, PlayersList,listaFotos)
    print(i+"--"+listaEquipos[cont]+"---"+listaFotos[cont])
    cont= cont+1


pasarAdb(listaEquipos,PlayersList,listaFotos)



