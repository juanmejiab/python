a = '   Hola juan'
b = 'Mundo'
n = 2

# Operadores para concatenar
print(a + b)
print(a, b)

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
print(a.upper())    # Imprime todo el string en mayuscula
print(a.lower())    # Imprime todo el string en minuscula
print(a.title())    # Imprime en mayuscula la primera letra de cada palabra
print(a.strip())    # Elimina espacios vacios al inicio de un string
print(a.replace(    # Cambia el contenido del primer argumento por el segundo
    'u', 'kj'))

# Indeces
print(a[0])         # Imprime el caracter en la posicion 0
print(a[-1])        # Imprime el caracter en la ultima posicion
print(a[0:3])       # Imprime los caracteres en un rango

a.split()  # Separar un string y convertirlo en lista
