



import requests
from bs4 import BeautifulSoup

import pandas as pd


# headers = {'User-Agent':
#   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

def scrapeofoto(indice,links,nombres,listafotos):

    url=links[indice]

    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    fotoscarnet=pageSoup.find_all("div",{"class": "dataBild"})[0].find_all("img")

    try:
        fotos=pageSoup.find_all("div",{"class": "galerie-content"})[0].find_all("img")
        listafotos.append(fotos[0]['data-src'])

    except:
        listafotos.append(fotoscarnet[0]['src'])














def scrapeo(url, players, prices, dorsales,links,equipo,listaequipos):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    """"
    A continuación encontrará en cada una de las etiquetas tr del sourcecode 
    las que coincidan con los parámetros que usamos como filtro en este caso
    los jugadores tienen asociado un atributo llamado athlete
    ocurre lo mismo para encontrar el precio del jugador en el que hay dos
    clases asociadas a los jugadores una que se llama rechts y otra llamada
    hauptlink
    """
    player = pageSoup.find_all("td", {"itemprop": "athlete"})
    price = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    dorsal = pageSoup.find_all("div", {"class": "rn_nummer"})
    link = pageSoup.select("td[class='hauptlink']",href=True)


    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores


    #print(link[0].find_all("a")[0]['href'])


    for i in link:

        links.append("https://www.transfermarkt.es"+i.find_all("a")[0]['href'])


    for i in player:
        players.append(i.text)
        listaEquipos.append(nombreEquipos[equipo])

    for i in price:
        prices.append(i.text)

    for i in dorsal:
        dorsales.append(i.text)





#descomentarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr


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

nombreEquipos={

    0: "\nA T L E T I C O\n",
    1: "\nB A R C E L O N A\n",
    2: "\nR E A L   M A D R I D\n",
    3: "\nS E V I L L A \n",
    4: "\nR E A L   S O C I E D A D\n",
    5: "\nV I L L A R R E A L\n",
    6: "\nV A L E N C I A\n",
    7: "\nA T H L E T I C\n",
    8: "\nB E T I S\n",
    9: "\nG E T A F E\n",
    10: "\nG R A N A D A\n",
    11: "\nC E L T A\n",
    12: "\nL E V A N T E\n",
    13: "\nA L A V E S\n",
    14: "\nO S A S U N A\n",
    15: "\nE I B A R\n",
    16: "\nV A L L A D O L I D\n",
    17: "\nH U E S C A\n",
    18: "\nC A D I Z\n",
    19: "\nE L C H E\n"



}

urlTransfermark = "https://www.transfermarkt.es/"


PlayersList = list()
ValuesList = list()
DorsalList = list()
linklist = list()
listaFotos = list()
listaEquipos = list()




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






for clave in urlTeamsLaliga:

    valor= nombreEquipos[clave]
    print(valor)
    scrapeo(urlTransfermark + urlTeamsLaliga[clave], PlayersList, ValuesList,DorsalList,linklist,clave,listaEquipos)

cont=0
for i in PlayersList:
    scrapeofoto(cont, linklist, PlayersList,listaFotos)
    print(i+"--"+listaEquipos[cont]+"---"+listaFotos[cont])
    cont= cont+1





