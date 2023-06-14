from pathlib import Path

ruta = Path("6-Python Standard Library")
ruta.exists()

# Crear un directorio
ruta.mkdir()

# Eliminar directorio
ruta.rmdir()

# Cambiar el nombre del directorio
ruta.rename("Ejemplo2")

# Obtener la lista de archivos y directorios en la ruta,
# retorna un generator object

# -------------------- Limitaciones --------------------
# 1. No se puede usar un patron de busqueda.
# 2. No busca recursivamente.
for p in ruta.iterdir():
    print(p)


rutas = [p for p in ruta.iterdir() if p.is_file()]
print(rutas)

# El metodo glob permite hacer busquedas de archivos segun un patron asignado
rutas = [p.name for p in ruta.glob("*.py")]
print(rutas)

# rglob permite buscar recursivamente todos los archivos contenidos en el
# directorio segun el criterio dado.
ruta2 = Path(r"C:\Users\juanm\Desktop\python\5-modulos")
rutas2 = [p.name for p in ruta2.rglob("*.py")]
print(rutas2)
