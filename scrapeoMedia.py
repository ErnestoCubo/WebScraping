# headers = {'User-Agent':
#   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
import sqlite3
import requests
from bs4 import BeautifulSoup

import pandas as pd

con = sqlite3.connect('equipos.db')
cursorObj=con.cursor()
cursorObj.execute('''CREATE TABLE EQUIPOS(Equipo TEXT, Jugadores INT, EdadMedia INT, ValorTotal FLOAT, ValorMedio FLOAT, Actualizacion TEXT)''')
con.commit()


def pasarAdb(resultado,num,edad,total,valor,actualizacion):

    con.execute('''INSERT INTO EQUIPOS(Equipo,Jugadores,EdadMedia,ValorTotal,ValorMedio,Actualizacion) VALUES(?, ?, ?, ?, ?, ?)''',
                  (resultado,num,edad,total,valor,actualizacion))
    con.commit()

    print("Informacion migrada a la DB")
#c.close()





def scrapeo(url):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    equipo = "local"
    resultado="local"

    aux =0
    actualizacion = "11-02-2021"
    totalValor=0
    totalEdad=0
    mediaEdad=0
    mediaValor=0

    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores


    for i in pageSoup.find_all("td", {"class": "rechts hauptlink"}):
        valor=i.text

        if (valor.find("€")==-1):
            valor2=0


        else:
            if (valor.find(",") == -1):
                split = valor.split(" ")
                valor = split[0]
                valor2 = float(valor)/1000
                totalValor+=valor2

            else:
                split = valor.split(',')
                valor = split[0]
                valor2 = int(valor)
                totalValor+=valor2
        aux+=1;

    mediaValor=totalValor/aux




    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):

        if (len(i.text) > 3):
            edad=i.text[12:14]
            edad2=int(edad)
            totalEdad+=edad2

    mediaEdad=totalEdad/aux;


    for i in pageSoup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['dataName']):
        equipo = i.text
        equipo = equipo.rstrip()
        resultado = equipo[2:len(equipo)]

    d = ({"Equipo": resultado,"Jugadores":aux, "Edad media": mediaEdad, "Valor total":totalValor, "Valor medio": mediaValor, "Actualizacion":actualizacion})

    df = pd.DataFrame(data=d, index=[0])


    print(df)

    pasarAdb(resultado,aux,mediaEdad,totalValor,mediaValor,actualizacion)






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


urlTransfermark = "https://www.transfermarkt.es/"



for clave in urlTeamsLaliga:

    scrapeo(urlTransfermark + urlTeamsLaliga[clave])
