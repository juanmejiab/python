import json
from pathlib import Path

peliculas = [
    {"id": 1, "titulo": "Spiderman", "ano": 2023},
    {"id": 2, "titulo": "Flash", "ano": 2023}
]

# Crear string con formato de archivo JSon a los datos
datos = json.dumps(peliculas)
Path(r"6-Python Standard Library\archivos\peliculas.json").write_text(datos)

# Leer datos de un archivo json
datos = Path(r"6-Python Standard Library\archivos\peliculas.json").read_text()
peliculas2 = json.loads(datos)
print(peliculas2)
