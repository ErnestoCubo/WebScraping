import sqlite3
import matplotlib.pyplot as plt

DATABASE = '.\equipos.db'

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
