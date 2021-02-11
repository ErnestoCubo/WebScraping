import sqlite3
import matplotlib.pyplot as plt

DATABASE = 'equipos.db'

conn = sqlite3.connect('equipos.db')
cur = conn.cursor()

cur.execute('select equipo from EQUIPOS')
conn.commit()

print(cur.fetchall())