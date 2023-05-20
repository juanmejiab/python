listas = ['Juan', 8, 'Pedro']  # Puede tener numeros o strings
listas.append(8.99)           # Añadir elementos a la lista
lista2 = listas.copy()        # Copiar lista
print(listas, lista2)

lista2.append(8)
lista2.count(8)               # Contar un elemento dado en la lista
print(len(lista2))            # Obtener la longitud de una lista
print(len(listas))
print(listas[0])             # Obtener el elemento de una lista seginm

listas.pop()                  # Eliminar el ultimo elemento de una lista
print(listas)

listas.remove('Juan')         # Eliminar un elemento especifico de la lista
print(listas)

listas.reverse()              # Ordena de atras para adelante una lista
print(listas)

lista3 = [5, 10, 1, 0.01, 22]
lista3.sort()                 # Ordena la lista de menor a mayor
print(lista3)
