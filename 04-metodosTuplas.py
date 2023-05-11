tupla = ('Juan', 8, 'Mejia')
print(tupla.index('Juan'))          # Retorna el indice en donde se encuentra el elemento
print(tupla.count('Juan'))          # Cuenta las veces que se repite el elemento

lista4 = list(tupla)                # Convierte tupla en una lista
lista4.append('Nuevo elemento de la tupla')
print(lista4)