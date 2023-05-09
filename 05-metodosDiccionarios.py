diccionario = {
    "nombre":"juan",
    "apellido":"perez",
    "edad":8
}

diccionario['nombre'] # Obtener el contenido de un elemento del diccionario

diccionario.get('nombre') # Obtener el contenido de un elemento del diccionario

diccionario['edad'] = 10 # Modificar un elemento del diccionario

len(diccionario) # Obtener la longitud del diccionario.

diccionario['ciudad']='Medellin' # Agregar elemento al diccionario

diccionario.pop('ciudad') # Eliminar un elemento del diccionario indicando la llave

diccionario.popitem() # Eliminar el ultimo elemento agregado al diccionario

del diccionario['apellido'] # Eliminar un elemento del diccionario indicando la llave

diccionario2 = diccionario.copy() # Sacar una copia del diccionario

diccionario2.clear() # Elimina todos los elementos del diccionario

# Diccionarios anidados

personas = {
    "Juan": {
        "nombre":"Juan Gomez",
        "edad":8
    },
    "Pedro":{
        "nombre":"Pedro Gonzalez",
        "edad":12
    }
}

personas['Juan']['nombre'] #Acceder a un valor de un diccionario anidado
personas.popitem()
personas.pop('Juan')