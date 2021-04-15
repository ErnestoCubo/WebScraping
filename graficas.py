import sqlite3
import matplotlib.pyplot as plt

DATABASE = 'equipos.db'

conn = sqlite3.connect('equipos.db')
cur = conn.cursor()

equipos_list = list()
precio_list = list()
for row in cur.execute('select equipo from EQUIPOS'):
    equipos_list.append(row[0])

resultado = cur.execute('select Valormedio from EQUIPOS where equipo=?', equipos_list)
con.commit()
for row in resultado:
    precio_list = row[0]
print(precio_list)

