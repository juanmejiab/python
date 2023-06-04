# Instanciar una clase
class Usuario:
    # Atributo de clase
    universidad = 'UPB'

    # Constructor de la clase
    def __init__(self, nombre: str, apellido: str, ciudad: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def saludo(self) -> str:
        return f'Hola! Mi nombre es {self.nombre} {self.apellido}'


# Instanciar un objeto de la clase
usuario1 = Usuario('Juan', 'Perez', 'Medellin')
usuario2 = Usuario('Pedro', "Lopez", 'Medellin')

# Crear nuevo atributo
usuario1.edad = 22
print(usuario1.edad)

# Indica si un objeto creado es insatancia de la clase indicada
print(isinstance(usuario1, Usuario))

# Acceder y modificar los atributos del objeto inatanciado
usuario1.nombre = 'Gonzalo'

# Acceder a un atributo de clase
print(Usuario.universidad)
print(usuario1.universidad)

# Modificar atributo de clase
Usuario.universidad = 'Eafit'
