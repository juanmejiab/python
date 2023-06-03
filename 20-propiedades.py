class Producto:

    def __init__(self, precio) -> None:
        self.precio = precio

    # getter
    @property
    def precio(self):
        return self.__precio

    # setter
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = valor


carro = Producto(10)
print(carro.precio)

carro.precio = -10
