from pathlib import Path
import shutil

ruta = Path(r"6-Python Standard Library\01-rutas.py")
ruta.exists()

# Renombrar el archivo
ruta.rename("init.txt")

# Eliminar el archivo
ruta.unlink()

# Obtener informacion del archivo
ruta.stat()

# Leer contenido del archivo (retorna un string con el contenido)
# Con este metodo, no hay que preocuparse por abrir el documento,
# cerrarlo y demas operaciones.
print(ruta.read_text())

# Copiar un archivo
origen = Path(
    r"C:\Users\juanm\Desktop\python\6-Python Standard Library\01-rutas.py")
destino = Path() / "prueba.py"

shutil.copy(origen, destino)
