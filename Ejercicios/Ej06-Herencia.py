class Animal:
    def __init__(self, nombre: str, raza: str) -> None:
        self.nombre = nombre
        self.raza = raza

    def saludar(self) -> str:
        return (f'Hola! Mi nombre es {self.nombre}, soy un {self.tipo} '
                f'y mi raza es {self.raza}')


class Gato(Animal):
    tipo = 'Gato'

    def __init__(self, nombre: str, raza: str,
                 onomatopeya: str) -> None:
        Animal.__init__(self, nombre, raza)
        self.onomatopeya = onomatopeya

    def maullar(self) -> str:
        return f'Soy {self.nombre} y mi sonido es {self.onomatopeya}'


class Perro(Animal):
    tipo = 'Perro'


labrador = Perro('Rush', 'Labrador')
siames = Gato('Tommy', 'Siames', 'Maullido')

labrador.saludar()

siames.saludar()
siames.maullar()
