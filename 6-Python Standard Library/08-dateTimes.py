import time
from datetime import datetime, timedelta

# -------------------------------- Time --------------------------------


def generador_numeros():
    for i in range(10000):
        pass


# time.time() -> retorna la fecha actual en segundos desde 1970 (linux)
inicio = time.time()
generador_numeros()
fin = time.time()

print(fin - inicio)


# ------------------------------ DateTime ------------------------------
# Crear una fecha
dt = datetime(2023, 6, 12)

# Fecha y hora actual
dt = datetime.now()

# Convertir string en fecha
dt = datetime.strptime("2023/06/12", "%Y/%m/%d")

# Convertir TimeStamp a DateTime
dt = datetime.fromtimestamp(time.time())

# Atributos
print(f"{dt.year}/{dt.month}")

# Convertir DateTime a string
print(dt.strftime("%Y/%m"))


# ----------------------------- Time Delta -----------------------------
dt1 = datetime(2002, 11, 11) + timedelta(1)
print(dt1)

dt2 = datetime.now()
duracion = dt2 - dt1

print(duracion)
print("dias", duracion.days)
print("segundos", duracion.seconds)
print("Total segundos", duracion.total_seconds())
