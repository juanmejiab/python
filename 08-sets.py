# Tipo 1: sets mutables
frutas = {'manzana', 'pera', 'mango', 'guanabana', 'mango'}
print(frutas)

# Funcion para crear un set (toma 1 argumento)
fruta = set('mango')
print(fruta)

# Tipo 2: sets inmutables
verduras = frozenset('Cebolla')
print(verduras)

# Metodos
frutas.add('guayaba')                   # Añadir elementos al set
print(frutas)

frutas.remove('guanabana')              # Eliminar elemento de un set
print(frutas)

frutas.pop()                            # Elimina el primer elemento del set
print(frutas)

frutas2 = frutas.copy()                 # Crea una copia del set
print(frutas2)

frutas2.clear()                         # Elimina todos los elementos del set
print(frutas2)

union = frutas.union(fruta)             # Union de dos sets (&)
print(union)

interseccion = frutas.intersection(     # Interseccion de dos sets (|)
    {'pera', 'guayaba', 'mango'}
)
print(interseccion)

# Retorna los elementos que no se repiten entre ambos
diferencia = frutas.difference(fruta)
print(diferencia)

diferencia_simetrica = frutas.symmetric_difference(
    fruta)  # Retorna la union de frutas y futa menos
print(diferencia_simetrica)                               # su interseccion

miSet = frutas.issuperset({'mango', 'pera'})
print(miSet)

miSet2 = {'mango', 'pera'}.issubset(frutas)
print(miSet2)
