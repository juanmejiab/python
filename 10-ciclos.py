# Ciclo while
n = 5

while n > 0:
    print(n)
    n -= 1

# Como interrumpir la ejecucion del ciclo
# antes de que termine
while n > 0:
    print(n)
    if n == 3:
        break
    n -= 1

# Palabra continue: deja de ejecutar las
# instrucciones que esten debajo y vuelve
# a la primera linea del ciclo
while n > 0:
    n -= 1
    if n == 3:
        continue
    print(n)

# Ciclo for

# Iteracion sobre listas
lista = ['Juan', 3, "Carro", 'Verde']

for x in lista:
    print(x)

# Iteracion sobre strings
cadena = 'Hola Mundo'

for x in cadena:
    print(x)

# Iteracion sobre diccionarios
diccionario = {
    'nombre': 'Juan',
    'edad': 20,
    'ciudad': 'Medellin'
}

for x in diccionario.values():
    print(x)

# Uso de condicionales dentro de un ciclo
exitoso = False
for x in range(1, 4):
    print('Intentando')
    if exitoso:
        print('Intento exitoso')
        break
else:
    print('El intento no fue exitoso')

# Ciclos anidados
for x in range(3):
    for y in range(2):
        print(f'({x}, {y})')
