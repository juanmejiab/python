import random
import string

# Genera numeros aleatorios entre 0 y 1
print(random.random())

# Numeros enteros aleatorios entre 1 y 10
print(random.randint(1, 10))

# Seleccionar numeros aleatorios en una lista
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Seleccionar varios numeros aleatorios en una lista
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=2))

# Seleccionar varios numeros aleatorios en un string
print(random.choices("abcdefghijk12345", k=4))

# Generador de contraseñas
print("".join(random.choices("abcdefghijk12345", k=4)))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# Cambiar el orden aleatoriamente de los elementos de una lista
numeros = [1, 2, 3, 4]
random.shuffle(numeros)
print(numeros)
