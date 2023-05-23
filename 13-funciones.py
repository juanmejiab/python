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


def nombre_completo(**kwargs: dict):
    print(kwargs['nombre'], kwargs['apellido'])


nombre_completo(
    nombre='Juan',
    apellido='Mejia'
)
