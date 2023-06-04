# La funcion print recibe 1 o muchos parametros
print('Hola', 'Mundo', ':)')

# Caracteres de escape

# \n --> Salto de línea
print('Hola \n Mundo')

# \t --> Tabulación
print('Hola \t Mundo')

# \x --> Caracter en hexadecimal
print('\xFF')

# \\ --> Backslash
print('Hola \\Mundo')

# \' --> Comilla simple
print('Hola \'Mundo')

# \" --> Comilla doble
print('Hola \"Mundo')

# \b --> Backspace
print('Hola \bMundo')

# Cómo dar formato a strings
nombre = 'Juan'
apellido = 'Mejía'

print('Mi nombre es {} {}'.format(nombre, apellido))
print('Mi nombre es %s %s ' % (nombre, apellido))
print(f'Mi nombre es {nombre} {apellido}')

# sep y end
# sep --> Completa los espacios de la concatenación con el caracter dado
print('Hola', 6, 'Mundo', sep='d')

# end --> Al final del print coloca el caracter dado
print('Hola mundo', end='k')
