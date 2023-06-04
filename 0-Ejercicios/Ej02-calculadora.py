# Calculadora que recibe por consola
# la operación a realizar y dos números

y = []
operando = ''

for x in range(1, 3):
    y.append(int(input(
        f'Ingrese el número {x}: '))
    )

operando = input('Ingrese la operación: ')


def operaciones(operador: str) -> float:
    if operador == '+':
        print('El resultado es:', float(y[0] + y[1]))
    elif operador == '-':
        print('El resultado es:', float(y[0] - y[1]))
    elif operador == '*':
        print('El resultado es:', float(y[0] * y[1]))
    elif operador == '/':
        print('El resultado es:', y[0] / y[1])
    else:
        print('Opción inválida.')
        op = input('Ingrese la operación: ')
        operaciones(op)


operaciones(operando)
