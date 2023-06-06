# Ejemplo sobre lectura de archivos locales y en linea usando herencia,
# solo se usa un nivel de herencia y clases abstractas

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Archivo(ABC):
    def __init__(self):
        self.abierto = False

    def abrir(self):
        if self.abierto:
            raise InvalidOperationError(
                "El archivo ya se encuentra abierto")
        self.abierto = True

    def cerrar(self):
        if self.abierto:
            raise InvalidOperationError(
                "El archivo ya se encuentra cerrado")
        self.abierto = False

    @abstractmethod
    def leer(self):
        pass


class ArchivoLocal(Archivo):
    def leer(self):
        print("Leyendo desde un archivo local")


class ArchivoLinea(Archivo):
    def leer(self):
        print("Leyendo desde un archivo en linea")


class ArchivoMemoria(Archivo):
    def leer(self):
        print("Leyendo archivo desde memoria.")


# Ejemplo polimorfismo
def leer(*archivos):
    for archivo in archivos:
        archivo.leer()


local = ArchivoLocal()
linea = ArchivoLinea()
memoria = ArchivoMemoria()

leer(local, linea, memoria)
