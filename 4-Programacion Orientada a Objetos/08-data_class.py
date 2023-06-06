# Clase que contiene un tipo de dato sin metodos
from collections import namedtuple


class Rectangulo:
    def __init__(self, largo, ancho) -> None:
        self.largo = largo
        self.ancho = ancho


rect1 = Rectangulo(1, 2)
rect2 = Rectangulo(1, 2)

# Esta comparacion retorna False porque no esta definido
# el metodo magico para comparalos
print(rect1 == rect2)


# Otra forma de lograr lo mismo
# La clase namedtuple contiene metodos magicos
Punto = namedtuple("Punto", ["x", "y"])
p1 = Punto(1, 2)
p2 = Punto(1, 2)

print(p1 == p2)
print(type(p1))
