# Instaciar una clase
class Usuario:
    # Constructor de la clase
    def __init__(self, nombre: str, apellido: str, ciudad: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def saludo(self) -> str:
        return f'Hola! Mi nombre es {self.nombre}'


# Instanciar un objeto de la clase
usuario1 = Usuario('Juan', 'Perez', 'Medellin')
usuario2 = Usuario('Pedro', "Lopez", 'Medellin')

# Acceder y modificar los atributos del objeto inatanciado
usuario1.nombre = 'Gonzalo'


# Clase con metodos
class Rectangulo:
    def __init__(self, largo: float, ancho: float) -> None:
        self.largo = largo
        self.ancho = ancho

    # Metodo que calcula el area del rectangulo
    def area(self) -> float:
        return self.largo*self.ancho


rect1 = Rectangulo(12.36, 5.36)
print(f'El area del rectangulo es {rect1.area()}')


# Herencia
class Administrador(Usuario):
    # Extendiendo el constructor de la clase padre
    def __init__(self, nombre: str, apellido: str, ciudad: str,
                 cargo: str) -> None:
        Usuario.__init__(self, nombre, apellido, ciudad)
        self.cargo = cargo

    def saludo_administrador(self) -> str:
        return (
            f'Hola! Mi nombre es {self.nombre}, soy administrador '
            f'y tengo el cargo de {self.cargo}.'
        )


admin = Administrador('Admnistrador', 'Feliz', 'Bogota', 'Lider fiducia')
print(admin.saludo())
print(admin.saludo_administrador())
