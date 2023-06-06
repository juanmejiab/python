# Formas de invocar el modulo
from operaciones.ventas import calcular_total
from operaciones import ventas

# Importanto sub modulos
from operaciones.inventario import inventario

valor = 20
cantidad = 2

print(f"El valor total es: {calcular_total(valor, cantidad)}")
inventario.mostrar_inventario()
