x = 9
y = 3

# Condicional
if x > y:
    print(f'{x} es mayor que {y}')

# Condicional con clausula else
if x > y:
    print(f'{x} es mayor que {y}')
else:
    print(f'{x} es menor que {y}')

# Condicional de una linea
if x > y:
    print(f'{x} es mayor que {y}')

# Condicional de una linea con else
print(f'{x} es mayor que y') if x > y else print(f"{x} es menor que {y}")

# Condicional anidado
if x > y:
    print(f"{x} es mayor que {y}")
elif x == y:
    print(f'{x} es igual a {y}')
else:
    print(f'{x} es menor que y')

# Concatenacion de operadores de comparacion
# Ejemplo: validar que la edad de una persona este entre los 18 y 65
edad = 20

if 18 <= edad < 65:
    print('La persona esta en el rango definido')
else:
    print('La persona no esta en el rango definido')
