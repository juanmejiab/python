valores = (x * 2 for x in range(10))

for x in valores:
    print(x)

# Operador para desempaquetar
# Sirve para obtener los valores individuales en cualquier iterador
# (menos diccionarios)
lista = [1, 2, 3]
lista2 = [3, 5]
combinada = [*lista, *"Hola", *lista2]
print(*lista)
print(combinada)

# Desempaquetando diccionarios
diccionario = {"x": 1}
diccionario2 = {"x": 10, "y": 2}

# En este caso, al tener 2 llaves iguales, el nuevo diccionario
# toma el valor del segundo
dicc_combinado = {**diccionario, **diccionario2, "z": 25}
print(dicc_combinado)
