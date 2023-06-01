# Clase con metodos
class Rectangulo:
    def __init__(self, largo: float, ancho: float) -> None:
        self.largo = largo
        self.ancho = ancho

    # Metodo de clase
    @classmethod
    def valor_defecto(cls) -> object:
        return cls(1, 2)

    # Metodos magicos (Ejemplo metodo str)
    def __str__(self) -> str:
        return f"({self.largo}, {self.ancho})"

    # Metodo para comparar objetos
    def __eq__(self, rectangulo: object) -> bool:
        return self.ancho == rectangulo.ancho and self.largo == rectangulo.largo

    def __gt__(self, rectangulo: object) -> bool:
        return self.ancho > rectangulo.ancho and self.largo > rectangulo.largo

    def __add__(self, rectangulo: object) -> bool:
        return Rectangulo(self.ancho + rectangulo.ancho,
                          self.largo + rectangulo.largo)

    # Metodo que calcula el area del rectangulo
    def area(self) -> float:
        return self.largo * self.ancho


rect1 = Rectangulo(12, 26)
print(f'El area del rectangulo es {rect1.area()}')

# Llamado al metodo de la clase
rect2 = Rectangulo.valor_defecto()
print(rect2.ancho, rect2.largo)

# Invocando metodo __str__
print(rect1)
print(str(rect1))

# Comparar objetos
print(rect1 == rect2)
print(rect1 > rect2)

# Operaciones aritmeticas
print(rect1 + rect2)
