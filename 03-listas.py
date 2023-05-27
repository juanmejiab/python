# Declaracion de listas
# Una lista puede tener numeros, strings u otra lista
listas = ['Juan', 8, 'Pedro']
matriz = [['Juan', 38.27], ['Pedro', 24], ['Lucas', 37.24]]

# Se puede crear una lista con elementos repetidos usando el operador *
zeros = [0] * 5
print(zeros)

# Tambien se pueden concatenar listas
lista_combinada = listas + zeros
print(lista_combinada)

# Acceder a elementos de una lista
print(lista_combinada[0])
print(lista_combinada[-1])

# Modificar elementos de una lista
lista_combinada[4] = 2.89

# Slicing
print(lista_combinada[0:3])
print(lista_combinada[:2])

# Desempaquetando listas
lista_desempaquetar1 = ['Juan', 1, 2, 3, 3, 4, 'Carro']
lista_desempaquetar2 = ['Juan', 4, 'Carro']

# Para desempaquetar la lista, puede hacerse de dos formas
# 1. Desempaquetando todos los elementos de la lista, esto creando
# tantas variables como elementos tenga la lista
primer_elemento, segundo_elemento, tercer_elemento = lista_desempaquetar2
print(primer_elemento, segundo_elemento, tercer_elemento)

# 2. Obtener algunos elementos de la lista
primer_elemento, segundo_elemento, *otros = lista_desempaquetar1
print(primer_elemento, segundo_elemento, otros)

primer_elemento, *otros, penultimo, ultimo = lista_desempaquetar1
print(primer_elemento, otros, penultimo, ultimo)

# Iteraciones sobre listas
for x in lista_desempaquetar1:
    print(x)

# Enumerando cada elemento de la lista, retorna una tupla
for x in enumerate(lista_desempaquetar1):
    print(x)

# Añadir elementos a la lista
listas.append(8.99)
listas.insert(1, 3.1415)
print(listas)

# Eliminar elementos de la lista
# El metodo pop puede recibir el indice del elemento que se quiera borrar
listas.pop()
print(listas)
listas.pop(1)
print(listas)

# Delete permite borrar un rango de elementos
del listas[0:3]
print(listas)

# El metodo clear elimina todos los elementos de una lista
listas.clear()
print(listas)

# El metodo remove permite ingresar un elemento de la lista y eliminarlo
listas.remove('Juan')
print(listas)

# Crear una copia de la lista
lista2 = listas.copy()
print(listas, lista2)

lista2.append(8)
lista2.count(8)               # Contar un elemento dado en la lista
print(len(lista2))            # Obtener la longitud de una lista
print(len(listas))


listas.reverse()              # Ordena de atras para adelante una lista
print(listas)

lista3 = [5, 10, 1, 0.01, 22]
lista3.sort()                 # Ordena la lista de menor a mayor
print(lista3)
