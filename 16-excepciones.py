# Manejar una sola excepcion
try:
    edad = int(input("Edad: "))
except ValueError as err:
    print("La edad ingresada no es valida.")
    print(err)
else:
    print("No hubo ninguna excepcion.")
print("Ejecucion finalizada.")

# Manejar multiples excepciones
try:
    edad = int(input("Edad: "))
    division = 10 / edad
except (ValueError, ZeroDivisionError) as err:
    print("La edad ingresada no es valida.")
    print(err)
else:
    print("No hubo ninguna excepcion.")

# Finally
# Ejemplo: uso de un archivo
try:
    archivo = open("app.py")
    edad = int(input("Edad: "))
    division = 10 / edad
except (ValueError, ZeroDivisionError) as err:
    print("La edad ingresada no es valida.")
    print(err)
finally:
    archivo.close()

# With
try:
    with open("app.py") as archivo:
        print("Archivo abierto")
    edad = int(input("Edad: "))
    division = 10 / edad
except (ValueError, ZeroDivisionError) as err:
    print("La edad ingresada no es valida.")
    print(err)


# Lanzar excepciones
def division(numero: int) -> float:
    if numero <= 0:
        raise ValueError("El numero no puede ser igual o menor a 0")
    return 10 / numero


try:
    division(0)
except ValueError as err:
    print(err)
