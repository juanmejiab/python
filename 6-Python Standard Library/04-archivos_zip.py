from pathlib import Path
from zipfile import ZipFile

# Crear un archivo .zip
# w: escribir
# r: unicamente leer
# x: unicamente crear
# a: añadir

with ZipFile("archivos.zip", "w") as zip:
    for ruta in Path("5-modulos").rglob("*.*"):
        zip.write(ruta)

# Leer archivos de un archivo zip
with ZipFile("archivos.zip") as zip:
    # Retorna el nombre de todos los archivos que contiene
    print(zip.namelist())

    # Obtener informacion de un archivo
    info = zip.getinfo("5-modulos/tienda.py")
    print(info.file_size)
    print(info.compress_size)

    # Extraer los archivos de un .zip
    # Opcionalmente se le puede indicar la ruta donde estaran los
    # archivos extraidos
    zip.extractall("6-Python Standard Library")
