class Dato:
    def __init__(self) -> None:
        # Atributo privado
        self.__valores = {}

    def add(self, valor) -> None:
        self.__valores[valor.lower()] = self.__valores.get(
            valor.lower(), 0) + 1

    def __getitem__(self, valor) -> int:
        return self.__valores.get(valor.lower(), 0)

    def __setitem__(self, valor, cantidad) -> None:
        self.__valores[valor.lower()] = cantidad

    def __len__(self):
        return len(self.__valores)

    def __iter__(self):
        return iter(self.__valores)


# Inicianizando el contenedor
contenedor = Dato()

# Pruebas de los metodos definidos
# Metodo add
contenedor.add("Python")
contenedor.add("Python")
contenedor.add("python")
print(contenedor.__valores)

# Metodo getitem
print(contenedor["python"])

# Metodo setitem
contenedor["python"] = 10

# Metodo len
print(len(contenedor))

# Metodo iter
for x in contenedor:
    print(x)
