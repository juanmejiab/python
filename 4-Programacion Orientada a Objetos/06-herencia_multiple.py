class Empleado:
    def saludar(self):
        print("Hola Empleado!")


class Persona:
    def saludar(self):
        print("Hola Persona!")


class Programador(Empleado, Persona):
    pass


programador1 = Programador()

# Al invocar el metodo saludar, la clase usa el metodo de la clase
# empleado porque es la primera clase colocada en la herencia
programador1.saludar()
