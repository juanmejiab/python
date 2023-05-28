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

# Obtener la longitud de una lista
print(len(lista_combinada))

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

# Del permite borrar un rango de elementos
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

# Hallar elementos de la lista
# El metodo index retorna la posicion del elemento ingresado
print(listas.index('Pedro'))

# El metodo count retorna la cantidad de veces que se repite un
# elemento de la lista
print(listas.count('Pedro'))

# Ordenando elementos de la lista
lista3 = [5, 10, 1, 0.01, 22]

# Ordena de atras para adelante una lista
lista3.reverse()
print(lista3)

# Ordenar la lista de menor a mayor
# Ordena los elementos dentro de la misma lista
lista3.sort()

# Este metodo retorna una nueva lista con los elementos ordenados
sorted(lista3)
print(lista3)

# Ordenar la lista de mayor a menor
lista3.sort(reverse=True)

# Este metodo retorna una nueva lista con los elementos ordenados
sorted(lista3, reverse=True)
print(lista3)

# Funcion lambda
items = [
    ('Producto1', 10),
    ('Producto2', 32),
    ('Producto3', 20)
]

# En este fragmento, Python toma cada elemento de la lista y lo pasa a
# la funcion definida, la cual retorna el elemento en la posicion 1 de la tupla
# que en este caso es el precio
items.sort(key=lambda item: item[1])
print(items)

# Funcion map
# La funcion map retorna un iterable
precios = list(map(lambda item: item[1], items))
print(precios)

# Funcion filter
filtro = list(filter(lambda item: item[1] >= 11, items))
print(filtro)
