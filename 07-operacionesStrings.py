a = 'Hola'
b = 'Mundo'
n = 2

# Operadores para concatenar
print(a + b)
print(a , b)

# Operador para replicar
print(a * n)

# Operador para saber si un string contiene a otro
c = "Holanda"
print(a in c)
print(a in b)

print(a not in c)
print(a not in b)

# Funciones
print(ord('a'))     # Retorna el Unicode de un solo caracter
print(chr(129363))  # Retorna el caracter a partidr del Unicode
print(len(a))       # Retorna la longitud de un string
print(str(2))       # Convierte un objeto en string

# Indeces
print(a[0])         # Imprime el caracter en la posicion 0
print(a[-1])        # Imprime el caracter en la ultima posicion
print(a[0:3])       # Imprime los caracteres en un rango

a.split() # Separar un string y convertirlo en lista
