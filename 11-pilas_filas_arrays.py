from collections import deque
from array import array

# --------------- Pilas ---------------
pila = []

# Añadir elementos a la cola de la pila
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

# Eliminar el ultimo elemento de la pila
pila.pop()
print(pila)

# --------------- Filas ---------------
fila = deque([])

# Añadir elementos a la fila
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)

# Eliminar los elementos de la fila
fila.popleft()
print(fila)

# --------------- Arrays ---------------
# Tienen los mismos metodos de una lista
numeros = array("i", [1, 2, 3])

# Añadir elementos a un array
numeros.append(4)
numeros.insert(1, 5)
print(numeros)

# Eliminar elementos de un array
numeros.pop()
numeros.remove(2)
print(numeros)
