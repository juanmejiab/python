class Animal:
    def __init__(self) -> None:
        self.edad = 1

    def comer(self):
        print("Comer")


class Mamifero(Animal):
    def __init__(self) -> None:
        # Implementa el constructor de la clase padre
        super().__init__()
        self.peso = 2

    def caminar(self):
        print("Caminar")


# Herencia multinivel: hereda de la clase mamifero y su vez de la clase
# animal
class Perro(Mamifero):
    pass


class Pez(Animal):
    def nadar(self):
        print("Nadar")


gato = Mamifero()
gato.comer()
print(gato.edad)

pez_payaso = Pez()
pez_payaso.comer()
print(pez_payaso.edad)

# Una instancia de una clase hija tambien es instancia de la clase padre
print(isinstance(gato, Animal))
print(isinstance(gato, Mamifero))
