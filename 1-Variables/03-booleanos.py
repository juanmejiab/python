# Los booleanos pueden ser dos tipos
verdadero = True
falso = False

# Los booleanos heredan operciones de
# los enteros (+, -, *, /)
print(verdadero + falso)

# Operadores
print(verdadero and falso)  # Ambos deben ser verdaderos para devolver True
print(verdadero or falso)  # Con que solo uno sea verdadero devuelve True
print(not verdadero)  # Retorna falso
print(not falso)  # Retorna verdadero

# Listas, diccionarios, tuplas, strings
# y sets vacios ademas del 0
# retornan False
numero = 0
lista = []
tupla = ()
diccionario = {}

print(bool(lista))
print(bool(tupla))
print(bool(diccionario))
print(bool(numero))
