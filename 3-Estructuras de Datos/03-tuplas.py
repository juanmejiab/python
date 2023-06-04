tupla = ('Juan', 8, 'Mejia')
lista = ['Juan', 8, 'Mejia']

# Convertir una lista en tupla
print(tuple(lista))

# Slicing
print(tupla[:2])

# Desempaquetado
x, y, z = tupla
print(x, y, z)

# Retorna el indice en donde se encuentra el elemento
print(tupla.index('Juan'))

# Cuenta las veces que se repite el elemento
print(tupla.count('Juan'))

# Convierte tupla en una lista
lista4 = list(tupla)
lista4.append('Nuevo elemento de la tupla')
print(lista4)
