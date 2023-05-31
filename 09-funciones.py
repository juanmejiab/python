# -------------Ejemplo 1-----------------
def suma(x: int, y: int, z: int) -> float:
    print(x + y/z)


# Llamado de la funcion
suma(4, 3, 6)

# Se pueden ingresar los argumentos en
# distinto orden indicandolos
suma(6, z=2, y=10)


# -------------Ejemplo 2-----------------
# Funcion que recibe varios argumentos
# retorna una tupla con los argumentos dados


def imprime_nombres(*nombre: str) -> tuple:
    for x in nombre:
        print(f'El nombre de la persona {nombre.index(x)+1} es {x}')


imprime_nombres('Juan', 'Carlos', 'Rodrigo',
                'Estefania', 'Mauricio', 'Fludian'
                )


# -------------Ejemplo 3-----------------


def sumatoria(*numeros: int) -> int:
    suma = 0
    for x in numeros:
        suma += x
    print(f'La sumatoria de los numeros es {suma}')


sumatoria(1, 5, 6, 9, 10, 14, 12, 11, 10, 20, 35, 28)


# -------------Ejemplo 4-----------------
# Uso de kwargs, usa la sintaxis de diccionario
# y retorna un diccionario


def nombre_completo(**kwargs: dict) -> dict:
    return (kwargs['nombre'], kwargs['apellido'])


datos = nombre_completo(
    nombre='Juan',
    apellido='Mejia'
)


# -------------Ejemplo 5-----------------
# Valor de parametro por defecto
# Al tenerlo por defeto no es obligatiorio
# ingresarlos todos


def multiplicacion(x: int, y: int, z=2) -> int:
    print(x*y*z)


multiplicacion(1, 2, 4)


# Uso de la palabra RETURN

# -------------Ejemplo 1-----------------
# Funcion que retorna la sumatoria de x numeros


def multiplicacion(*numeros: int) -> int:
    mult = 1
    for x in numeros:
        mult *= x
    return mult


resultado_mult = multiplicacion(1, 5, 3, 6, 9, 7, 10)
print(f'El resultado de la multiplicacion es {resultado_mult}')


# -------------Ejemplo 2-----------------
# Funcion que retorna los datos de una persona


def datos_usr(**kwargs: dict) -> dict:
    return kwargs


datos = datos_usr(
    nombre='Juan',
    apellido="Mejia",
    telefono='3102221234'
)

print('Mi nombre es %s, mi apellido %s y mi telefono %s' %
      (datos['nombre'], datos['apellido'], datos['telefono']))


# -------------Recursion---------------
# Consiste en invocar una funcion dentro
# de si misma


def recursion(i: int) -> int:
    if (i < 2):
        return i
    print(i)
    recursion(i-1)


recursion(5)
