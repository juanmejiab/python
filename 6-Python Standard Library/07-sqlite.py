import sqlite3
import json
from pathlib import Path

peliculas = json.loads(
    Path(r"6-Python Standard Library\archivos\data.csv").read_text())

with sqlite3.connect(r"6-Python Standard Library\archivos\cine.sqlite3") as conn:
    # Creacion de una sentencia que luego sera ejecutada para hacer cambios a
    # la base de datos, los signos de interrogacion su usan para mas adelante
    # indicar los valores que tendran.
    sentencia = "INSERT INTO Peliculas VALUES(?, ?, ?)"
    for pelicula in peliculas:
        conn.execute(sentencia, tuple(pelicula.values()))
    conn.commit()

# Leer datos desde la base de datos
with sqlite3.connect(r"6-Python Standard Library\archivos\cine.sqlite3") as conn:
    sentencia = "SELECT * FROM Peliculas"
    cursor = conn.execute(sentencia)
    cursor.fetchall()
