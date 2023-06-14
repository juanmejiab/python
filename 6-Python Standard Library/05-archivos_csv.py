import csv

# Escribir en archivos csv
# En newline se especifica que no se dejen espacios en blanco entre cada linea
with open(r"6-Python Standard Library\archivos\data.csv", "w", newline="") \
        as archivo:
    # Generar un "Escritor" para el archivo csv, esto
    # permite que se pueda escribir en el
    escritor = csv.writer(archivo)
    escritor.writerow(["id", "producto", "precio"])
    escritor.writerow([1, "carro", 10])
    escritor.writerow([2, "carro", 12])
    escritor.writerow([3, "carro", 15])

# Leer archivos csv
with open(r"6-Python Standard Library\archivos\data.csv") as archivo:
    lector = csv.reader(archivo)
    print(list(lector))
