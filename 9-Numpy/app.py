import numpy as np

array = np.array([1, 2, 3])
print(array)
print(array.shape)

# Matriz de 2 filas y 3 columnas
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.shape)

# Matriz de 0s
matrix2 = np.zeros((3, 4), dtype=int)
print(matrix2)

# Matriz de 1s
matrix3 = np.ones((3, 4), dtype=int)
print(matrix3)

# Matriz con valor personalizado
matrix4 = np.full((3, 4), 6, dtype=int)
print(matrix4)

# Matriz con numeros aleatorios
matrix5 = np.random.random((3, 4))
print(matrix5)

# Acceder a elementos del arreglo
print(matrix5[0, 1])


# -------------- Opereaciones --------------
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])

# Suma
print(first + 2)
print(first + second)

# Resta
print(first - second)

# Multiplicacion
print(first * second)

# Division
print(first / second)
