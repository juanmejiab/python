from pathlib import Path

# Ruta en windows
Path(r"C:\Program Files\Microsoft")

# Ruta en linux
Path("/usr/local/bin")

# Referencia a la carpeta actual
Path()

# Ruta relativa
Path("ecommerce/__init__.py")

# Combinar rutas
Path() / "ecommerce" / "__init__.py"

# Directorio principal del usuario actual
Path.home()

ruta = Path(
    r"C:\Users\juanm\Desktop\python\6-Python Standard Library\01-rutas.py")

# Metodos
# Verificar si una ruta existe
ruta.exists()

# Verificar si la ruta representa un archivo
ruta.is_file()

# Verificar si la ruta representa un directorio
ruta.is_dir()

# Imprimir el nombre del archivo
print(ruta.name)

# Imprimir el nombre del archivo sin la extension
print(ruta.stem)

# Imprimir la extension del archivo
print(ruta.suffix)

# Imprimir la ruta padre del archivo
print(ruta.parent)

# Crear un nuevo objeto ruta basado en la ruta existente
# y solo cambiar el nombre y la extension del archivo
ruta2 = ruta.with_name("archivo.txt")
print(ruta2)

# Cambiar solo la extension de un archivo
ruta2 = ruta.with_suffix(".txt")
print(ruta2)
