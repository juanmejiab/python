tupla = ('Juan', 8, 'Mejia')
# Retorna el indice en donde se encuentra el elemento
print(tupla.index('Juan'))
# Cuenta las veces que se repite el elemento
print(tupla.count('Juan'))

lista4 = list(tupla)                # Convierte tupla en una lista
lista4.append(
    'Nuevo elemento \
    de la tupla'
)
print(lista4)
