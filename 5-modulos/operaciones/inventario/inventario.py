# Invocar submodulos
# Forma absoluta (Recomendada si no es muy larga)
from operaciones.cliente import clientes

# Forma relativa
from ..cliente import clientes


clientes.mostrar_clientes()


def mostrar_inventario():
    print("Hay 4 camisetas disponibles")
